from src.courses import CourseList
from datetime import datetime


season = "spring"
now = datetime.now()
term = ''

if season.lower() == 'spring':
    term = f'{now.year + 1}' + '02' if now.month > 4 else f'{now.year}' + '02'
else:
    term = f'{now.year}' + '05' if season.lower() == 'summer' else f'{now.year}' + '08'


crns = []  # classes crn for example, ['86991', '86992', '82928', '88421']
lst = CourseList(crns, term)
print("\n\n")

email_from = ""
email_to = ""
email_password = ""  # Not the password but the automated password, more in readme.md
phone_number_in_email_format = ""
lst.run_notifier_email(email_from, email_password, phone_number_in_email_format, email_to)

import argparse
from src.courses import CourseList
from datetime import datetime


def main():
    parser = argparse.ArgumentParser(description="Automate course notifications.")

    # Required arguments
    parser.add_argument('--season', type=str, required=True, choices=['spring', 'summer', 'fall'],
                        help="Specify the season (e.g., 'spring', 'summer', 'fall').")
    parser.add_argument('--crns', type=str, nargs='+', required=True,
                        help="List of CRNs for the courses (e.g., '86991 86992 82928').")
    parser.add_argument('--email_from', type=str, required=True, help="Sender email address.")
    parser.add_argument('--email_password', type=str, required=True, help="Automated email password.")

    # Optional arguments
    parser.add_argument('--phone_number_in_email_format', type=str, default='',
                        help="Optional: Phone number in email format for SMS notifications.")
    parser.add_argument('--email_to', type=str, default='',
                        help="Optional: Recipient email address. If none is provided, email_from is the default recipient")

    args = parser.parse_args()

    # Determine term code based on season and current month/year
    now = datetime.now()
    if args.season.lower() == 'spring':
        term = f'{now.year + 1}02' if now.month > 4 else f'{now.year}02'
    elif args.season.lower() == 'summer':
        term = f'{now.year}05'
    else:
        term = f'{now.year}08'

    # Create CourseList object with provided CRNs and term
    lst = CourseList(args.crns, term)
    print("\n\n")

    # Run notifier with command-line provided email details
    lst.run_notifier_email(args.email_from, args.email_password, args.phone_number_in_email_format, args.email_to)


if __name__ == "__main__":
    main()
