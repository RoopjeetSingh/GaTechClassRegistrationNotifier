from src.courses import Course, CourseList
from datetime import datetime


season = "fall"
now = datetime.now()
term = ''

if season.lower() == 'spring':
    term = f'{now.year + 1}' + '02' if now.month > 4 else f'{now.year}' + '02'
else:
    term = f'{now.year}' + '05' if season.lower() == 'summer' else f'{now.year}' + '08'


crns = []  # classes crn for example, ['86991', '86992', '82928', '88421']
courses = [Course(crn, term) for crn in crns]
print("\n\n")
lst = CourseList(courses)

email_from = ""
email_to = ""
email_password = ""  # Not the password but the automated password, more in readme.md
phone_number_in_email_format = ""
lst.run_notifier_email(email_from, email_password, phone_number_in_email_format, email_to)
