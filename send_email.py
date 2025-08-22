# -*- coding: utf-8 -*-
#
# send_email.py
# This script sends a test email with minimal content.
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

# Use a subject and body with no spaces or special characters.
subject = 'Test'
body = 'Test'

# Create a secure SSL context
context = ssl.create_default_context()

# Create the email message object
message = MIMEText(body, "plain", "utf-8")
message["Subject"] = subject
message["From"] = sender_email
message["To"] = receiver_email

print("Starting email script execution...")
print(f"Subject: '{subject}'")
print(f"Body: '{body}'")

try:
    # Connect to the SMTP server securely
    print("Attempting to connect to SMTP server...")
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        print("Connection secured. Logging in...")
        server.login(sender_email, password)
        print("Login successful. Sending email...")
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")

except Exception as e:
    print(f"An error occurred!")
    print(f"Error details: {e}")
