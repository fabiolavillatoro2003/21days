# -*- coding: utf-8 -*-
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

# Define the subject. This will still be plain text.
subject = f'Daily Cold Plunge Reminder for {today}'

# Define the body as an HTML string
body = """
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<style>
  body {{ font-family: sans-serif; }}
  h1 {{ color: #1a237e; }}
  p {{ font-size: 16px; }}
</style>
</head>
<body>
<h1>Daily Cold Plunge Reminder!</h1>
<p>Hey there,</p>
<p>DID YOU DO YOUR COLD PLUNGE?!?!?!</p>
<p>Love,<br>yourself</p>
</body>
</html>
"""

# Try to initialize yagmail and send the email
try:
    yag = yagmail.SMTP(sender, password)
    # The 'contents' parameter can take an HTML string, which forces UTF-8 encoding.
    yag.send(to=recipient, subject=subject, contents=body)
    print("Email sent successfully!")

except Exception as e:
    # If an error occurs, print it to the GitHub Actions log
    print(f"Error sending email: {e}")

