# -*- coding: utf-8 -*-
#
# send_email.py
# This script sends an email reminder using yagmail.
#

import yagmail
import os
import datetime
import unicodedata

# Function to remove all special characters and problematic whitespace
def clean_string(s):
    # Normalize the string to a decomposed form (e.g., convert 'é' to 'e' + accent).
    # Then, encode to ASCII, ignoring any characters that can't be mapped.
    # Finally, decode back to a standard string.
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode('ascii')
    # Replace all remaining whitespace with a single space and remove leading/trailing spaces.
    return ' '.join(s.split()).strip()

# Get the email password from the GitHub Actions environment variable
password = os.environ.get('EMAIL_PASSWORD')

# Set up the sender and recipient. Use your email address for both.
sender = 'fvillatoro99@gmail.com'
recipient = 'fvillatoro99@gmail.com'

# Get the current date to include in the email subject
today = datetime.date.today().strftime('%B %d, %Y')

# Define the subject and body of the email.
# The `today` variable is the most likely source of problematic characters.
subject_raw = f'Daily Cold Plunge Reminder for {today}'
body_raw = """
Hey there,

DID YOU DO YOUR COLD PLUNGE?!?!?!?

Love,
yourself
"""

# Clean the subject and body to ensure no problematic characters are present
subject = clean_string(subject_raw)
body = clean_string(body_raw)

# Try to initialize yagmail and send the email
try:
    yag = yagmail.SMTP(sender, password)
    yag.send(to=recipient, subject=subject, contents=body)
    print("Email sent successfully!")

except Exception as e:
    # If an error occurs, print it to the GitHub Actions log
    print(f"Error sending email: {e}")
