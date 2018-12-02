
import os

from flask import render_template
from flask_mail import Message

import sendgrid
from sendgrid.helpers.mail import *

from app import create_app
from app import config
from config import config

print("Starting Mail Test")
print(os.getenv('MAIL_SENDGRID_API_KEY'))

sg = sendgrid.SendGridAPIClient(apikey=os.getenv('MAIL_SENDGRID_API_KEY'))

def send_email(recipient, subject, template, **kwargs):

    print(recipient)
    print('&&&&&&&&&&&')
    app = create_app(os.getenv('FLASK_CONFIG') or 'default')
    with app.app_context():
        
        sg = sendgrid.SendGridAPIClient(apikey='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')
        from_email = Email(app.config['EMAIL_SENDER'])
        print(from_email)

        to_email = Email(recipient)
        print('******')
        print(to_email)
        subject = app.config['EMAIL_SUBJECT_PREFIX'] + ' ' + subject
        print(subject)
        # content = render_template('account/email/invite' + '.html', **kwargs)
        content = "This is the content"
        print(content)
        mail = Mail(from_email,subject,to_email,content)
        # response = sg.client.mail.send.post(request_body=mail.get())
        print(response)


print("Sending mail")
template =  "sub" + ' ' + "subject"
send_email("geody.moore@gmail.com","This is the subject",template)

