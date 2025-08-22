# -*- coding: utf-8 -*-
#
# send_email.py
# This script sends an email reminder using Python's standard libraries.
#

import os
import smtplib
import ssl
from email.mime.text import MIMEText

# Get the email password from the GitHub Actions environment variable
password = os.environ.get('EMAIL_PASSWORD')

# Set up the sender and recipient
sender_email = 'fvillatoro99@gmail.com'
receiver_email = 'fvillatoro99@gmail.com'

# Define the SMTP server and port for Gmail
smtp_server = "smtp.gmail.com"
port = 587  # For starttls

# Define the subject and body of the email.
# We will use clean, plain strings. The encoding is handled by MIMEText.
subject = 'Daily Cold Plunge Reminder for today'
body = """
Hey there,

DID YOU DO YOUR COLD PLUNGE?!?!?!?

Love,
yourself
"""

# Create a secure SSL context
context = ssl.create_default_context()

# Create the email message object
# We explicitly set the charset to UTF-8 here.
message = MIMEText(body, "plain", "utf-8")
message["Subject"] = subject
message["From"] = sender_email
message["To"] = receiver_email

print("Starting email script execution...")
print(f"Subject: {subject}")
print(f"Body: {body[:30]}...")

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
