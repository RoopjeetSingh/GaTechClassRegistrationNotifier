import smtplib
from email.message import EmailMessage
from datetime import datetime

import requests
import time
from bs4 import BeautifulSoup


def send_email(email_from: str, email_password: str, content: str, classes: list,
               phone_number_as_email: str = "", email_to: str = ""):
    msg = EmailMessage()
    msg.set_content(content)
    msg['subject'] = "Courses Open- " + ', '.join(classes)
    if phone_number_as_email:
        msg['to'] = phone_number_as_email
        msg['cc'] = email_to or email_from
    else:
        msg['to'] = email_to or email_from
    msg['from'] = email_from

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email_from, email_password)
    server.send_message(msg)

    server.quit()


class Course:
    def __init__(self, crn: str, term: str):
        self.crn = crn
        self.term = term  # default
        url = 'https://oscar.gatech.edu/bprod/bwckschd.p_disp_detail_sched?term_in='
        url += self.term + '&crn_in=' + self.crn
        with requests.Session() as s:
            with s.get(url) as page:
                soup = BeautifulSoup(page.content, 'html.parser')
                headers = soup.find_all('th', class_="ddlabel")
                self.name = headers[0].getText()
                print(self.name)

    def has_name(self) -> bool:
        return self.name is not None

    def __get_registration_info(self, term: str):
        url = 'https://oscar.gatech.edu/bprod/bwckschd.p_disp_detail_sched?term_in='
        url += term + '&crn_in=' + self.crn

        with requests.Session() as s:
            with s.get(url) as page:
                soup = BeautifulSoup(page.content, 'html.parser')
                table = soup.find('caption', string='Registration Availability').find_parent('table')

                if len(table) == 0:
                    raise ValueError()

                data = [int(info.getText()) for info in table.findAll('td', class_='dddefault')]
                return data

    def get_registration_info(self, term: str):
        self.term = term
        data = self.__get_registration_info(term)

        if len(data) < 6:
            raise ValueError()

        waitlist_data = {
            'seats': data[3],
            'taken': data[4],
            'vacant': data[5]
        }
        load = {
            'seats': data[0],
            'taken': data[1],
            'vacant': data[2],
            'waitlist': waitlist_data
        }
        return load

    def is_open_by_term(self, term: str) -> bool:
        return self.__get_registration_info(term)[2] > 0

    def is_open(self) -> bool:
        return self.is_open_by_term(self.term)

    def waitlist_available_by_term(self, term: str) -> bool:
        waitlist_data = self.get_registration_info(term)['waitlist']
        return waitlist_data['vacant'] > 0

    def waitlist_available(self) -> bool:
        return self.waitlist_available_by_term(self.term)

    def __str__(self) -> str:
        data = self.get_registration_info(self.term)
        res = "{}\n".format(self.name)
        for name in data:
            if name == 'waitlist':
                continue
            res += "{}:\t{}\n".format(name, data[name])
        res += "waitlist open: {}\n".format('yes' if self.waitlist_available() else 'no')
        return res


class CourseList:
    def __init__(self, courses, term):
        now = datetime.now()
        if term.lower() == 'spring':
            term = f'{now.year + 1}02' if now.month > 4 else f'{now.year}02'
        elif term.lower() == 'summer':
            term = f'{now.year}05'
        else:
            term = f'{now.year}08'
        self.courses = [Course(crn, term) for crn in courses]

    def send_email_notify(self, email_from: str, email_password: str, phone_number_as_email: str = "", email_to: str = ""):
        body = ""
        names = []
        courses_to_remove = []
        for course in self.courses:
            if course.is_open():
                body += course.__str__() + "\n"
                names.append(course.name)
                courses_to_remove.append(course)
            time.sleep(0.025)

        for course in courses_to_remove:
            self.courses.remove(course)

        if body:
            print("\nCourses Opened: \n" + body)
            # print([course.name for course in self.courses])

            send_email(email_from, email_password, body, names, phone_number_as_email, email_to)

    def run_notifier_email(self, email_from: str, email_password: str, phone_number_as_email: str = "", email_to: str = ""):
        while self.courses:
            self.send_email_notify(email_from, email_password, phone_number_as_email, email_to)
            time.sleep(60)  # check every minute
