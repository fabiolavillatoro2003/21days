# -*- coding: utf-8 -*-
#
# send_email.py
# This script sends an email reminder using Python's standard libraries.
#

import os
import smtplib
import ssl
from email.mime.text import MIMEText
import datetime
import unicodedata

def clean_string(s):
    """Replaces all non-standard spaces with a regular space and removes leading/trailing whitespace."""
    s = s.replace(u'\xa0', ' ') # Specifically replace non-breaking spaces
    return ' '.join(s.split()).strip()

# Get the email password from the GitHub Actions environment variable
password = os.environ.get('EMAIL_PASSWORD')

# Set up the sender and recipient
sender_email = 'fvillatoro99@gmail.com'
receiver_email = 'fvillatoro99@gmail.com'

# Define the SMTP server and port for Gmail
smtp_server = "smtp.gmail.com"
port = 587  # For starttls

# Define the subject and body of the email.
subject_raw = f'Daily Cold Plunge Reminder for {datetime.date.today().strftime("%B %d, %Y")}'
body_raw = """
Hey there,

DID YOU DO YOUR COLD PLUNGE?!?!?!?

Love,
yourself
"""

# Programmatically clean the strings
subject = clean_string(subject_raw)
body = clean_string(body_raw)

print("Starting email script execution...")
print(f"Subject: '{subject}'")
print(f"Body (first 30 chars): '{body[:30]}...'")

# Create a secure SSL context
context = ssl.create_default_context()

# Create the email message object
message = MIMEText(body, "plain", "utf-8")
message["Subject"] = subject
message["From"] = sender_email
message["To"] = receiver_email

try:
    # Connect to the SMTP server securely
    print("Attempting to connect to SMTP server...")
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)  # Secure the connection
        print("Connection secured. Logging in...")
        server.login(sender_email, password)
        print("Login successful. Sending email...")
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")

except Exception as e:
    # Print the full error for debugging
    print(f"An error occurred!")
    print(f"Error details: {e}")
