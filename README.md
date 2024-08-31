# GaTechClassRegistrationNotifier
Given CRNs of classes, the program sends an email as well as text message when the classes open

To use:

1. Clone the Github Reprository

2. Change the list "crns" to include the CRNs for which you want to recieve updates

As of 2024, this is what works as email and password:

Go to https://myaccount.google.com/security and make sure 2-step verification in enabled on your account. So for this you can setup an app on your phone like Google Authenticator, authy etc..

Once you have setup "2-Step Verification", from security go to "2-Step verification" again and scroll down to "App Passwords":

![image](https://github.com/user-attachments/assets/bddd34a2-4a71-49cd-bc35-313f78f458f9)

Now give your app a name and you will be given a password for your device.

Finally save your password somewhere safe and plugin your email and password into the email_from and email_password variables

To get your phone number in the email format, go to https://www.notepage.net/smtp.htm and check your provider. For example T-Mobile phone numbers can be written as number@tmomail.net

Alternatively, search your provider as email in google to check the SMTP Gateway

Input this as the phone_number_in_email_format variable and run the program
