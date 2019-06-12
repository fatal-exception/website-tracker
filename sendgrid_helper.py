from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os


def send_mail(message):
    message = Mail(
        from_email='matt@lydiaralph.com',
        to_emails='ralpmat@gmail.com',
        subject='Website tracker',
        plain_text_content=message)
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)
