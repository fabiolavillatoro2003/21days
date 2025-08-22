import yagmail
import os
import datetime

password = os.environ.get('EMAIL_PASSWORD')
sender = 'fvillatoro99@gmail.com'
recipient = 'fvillatoro99@gmail.com'

today = datetime.date.today().strftime('%B %d, %Y')

subject = f'DAILY COLD PLUNGE REMINDER FOR {today}'
body = """

test

"""

try:
    yag = yagmail.SMTP(sender, password)
    yag.send(to=recipient, subject=subject, contents=body)
    print("Email sent success")

except Exception as e:
    print("Error sending email: {e}")