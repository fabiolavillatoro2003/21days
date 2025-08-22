#
# send_email.py
#
import yagmail
import os
import datetime

print("Starting email script execution...")

# Get the email password from the GitHub Actions environment variable
password = os.environ.get('EMAIL_PASSWORD')
print(f"Retrieved password from environment variable. Length: {len(password)}")

# Set up the sender and recipient
sender = 'fvillatoro99@gmail.com'
recipient = 'fvillatoro99@gmail.com'
print(f"Sender: {sender}, Recipient: {recipient}")

# Get the current date to include in the email subject
today = datetime.date.today().strftime('%B %d, %Y')
print(f"Formatted date: {today}")

# Define the subject and body of the email
subject = f'Daily Cold Plunge Reminder for {today}'
body = """
Hey there,

DID YOU DO YOUR COLD PLUNGE?!?!?!?

Love,
yourself
"""
print(f"Subject: {subject}")
print(f"Body (first 20 chars): {body[:20]}...")

# Try to initialize yagmail and send the email
try:
    print("Attempting to connect to SMTP server...")
    yag = yagmail.SMTP(sender, password)
    print("SMTP connection successful. Attempting to send email...")
    yag.send(to=recipient, subject=subject, contents=body)
    print("Email sent successfully!")

except Exception as e:
    # Print the full error for debugging
    print(f"An error occurred!")
    print(f"Error details: {e}")
    # You can also add more specific error handling here