import argparse
from courses import CourseList
import re

def validate_crns(crns):
    """Ensure all CRNs are 5-digit numbers."""
    if not all(re.fullmatch(r'\d{5}', crn) for crn in crns):
        raise argparse.ArgumentTypeError("Each CRN must be a 5-digit number.", crns)
    return crns


def validate_email(email):
    """Ensure email is in valid format."""
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    if email and not re.fullmatch(email_pattern, email):
        raise argparse.ArgumentTypeError("Invalid email format.")
    return email

def validate_phone_email_format(phone_email):
    """Ensure phone number in email format is valid."""
    if phone_email and not validate_email(phone_email):
        raise argparse.ArgumentTypeError("Invalid phone number email format.")
    return phone_email

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
    email_password = args.email_password.replace('\xa0', ' ')
    # Create CourseList object with provided CRNs and term
    lst = CourseList(args.crns, args.season.lower())
    print("\n\n")

    # Run notifier with command-line provided email details
    lst.run_notifier_email(args.email_from, email_password, args.phone_number_in_email_format, args.email_to)


if __name__ == "__main__":
    main()
