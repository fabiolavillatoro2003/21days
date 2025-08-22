#
# send_email.py
# This script sends an email reminder using yagmail.
#

import yagmail
import os
import datetime

# Get the email password from the GitHub Actions environment variable
password = os.environ.get('EMAIL_PASSWORD')

# Set up the sender and recipient. Use your email address for both.
sender = 'fvillatoro99@gmail.com'
recipient = 'fvillatoro99@gmail.com'

# Get the current date to include in the email subject
today = datetime.date.today().strftime('%B %d, %Y')

# Define the subject and body of the email.
# Ensure no invisible characters are present.
#subject = f'Daily Cold Plunge Reminder for {today}'
subject = f'Daily Cold Plunge Reminder for {today}'.encode('utf-8')

# body = """
# Hey there,

# DID YOU DO YOUR COLD PLUNGE?!?!?!?

# Love,
# yourself
# """
body = """
Hey there,

DID YOU DO YOUR COLD PLUNGE?!?!?!?

Love,
yourself
""".encode('utf-8')

# Try to initialize yagmail and send the email
try:
    yag = yagmail.SMTP(sender, password)
    yag.send(to=recipient, subject=subject, contents=body)
    print("Email sent successfully!")

except Exception as e:
    # If an error occurs, print it to the GitHub Actions log
    print(f"Error sending email: {e}")

