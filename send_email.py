import yagmail
import os
import datetime

#secret
password = os.environ.get('EMAIL_PASSWORD')

# Set up the sender and recipient
sender = 'fvillatoro99@gmail.com'  
recipient = 'fvillatoro99@gmail.com' 

# Get the current date to include in the email
today = datetime.date.today().strftime('%B %d, %Y')

# Define the subject and body of the email
subject = f'Daily Cold Plunge Reminder for {today}'
body = """
Hey there,

DID YOU DO YOUR COLD PLUNGE?!?!?!?

Love,
yourself
"""

try:
    # Initialize yagmail with your email and the password from the secret
    yag = yagmail.SMTP(sender, password)

    # Send the email
    yag.send(to=recipient, subject=subject, contents=body)
    print("Email sent successfully!")

except Exception as e:
    # Print any errors that occur
    print(f"Error sending email: {e}")

