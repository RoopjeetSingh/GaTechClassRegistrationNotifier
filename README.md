# GaTechClassRegistrationNotifier
Given CRNs of classes, the program sends an email as well as text message when the classes open

To use you should have python installed:

1. Clone the Github Reprository

2. Install the libraries listen in requirements.txt using `pip install -r requirements.txt`
   
3. Get the email and password for automation 
   Your email account must support automation. Follow these steps to enable it:

   ### Steps to Set Up an App Password (for Gmail as of 2024)
   
   1. Go to [Google Account Security](https://myaccount.google.com/security).
   2. Enable **2-Step Verification** on your account:
      - Set up 2-Step Verification using an authenticator app like Google Authenticator or Authy.
   
   3. After enabling **2-Step Verification**, return to the **Security** settings and navigate to **2-Step Verification**.  
      Scroll down to find **App Passwords**.
   
   ![App Passwords Example](https://github.com/user-attachments/assets/bddd34a2-4a71-49cd-bc35-313f78f458f9)
   
   4. Create an app password:
      - Select an app name and generate the password for your device.
      - Save this password somewhere secure. You will use it in the next step (Step 4) for the program.

   ### Finding Your Phone Number’s Email Format
   1. Go to [NotePage's SMTP Gateway List](https://www.notepage.net/smtp.htm) to find your provider.
   2. For example, T-Mobile phone numbers can be formatted as `number@tmomail.net`.
   3. Alternatively, you can search for your provider’s email format on Google by searching for "`[Your Provider] email format`".


4. After getting the password, use the command line to start the notifier:

   Run `python3 send_email_tracker.py` with the following commands:

   - `--season:`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spring, fall, or summer
   - `--email_from:`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;the email that was just automated using the 3rd step
   - `--email_password:`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The password that you received in the 3rd step (App Passwords)
   - `--crns:`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A list of CRNs that you want to track. For example `--crns 32128 20982 29922 21289 29919`
   - `--email_to:`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;An optional argument; this is the email address to which the email should be sent. If empty, the email will be sent to the email provided during `email_from`
   - `--phone_number_in_email_format:` An optional argument; this is the phone number in email format. As given in step 3, you can get it by going to https://www.notepage.net/smtp.htm and checking your provider or just searching your provider as email in Google.

For example, here is a sample command line argument  
`python send_email_tracker.py --season spring --crns 32128 20982 29922 21289 29919 --email_from emailFrom@gmail.com --email_password "passwordInQuotesForSpaces" --email_to emailTo@gmail.com --phone_number_in_email_format number@tmomail.net`
