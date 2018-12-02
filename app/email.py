
import os

from flask import render_template

import sendgrid
from sendgrid.helpers.mail import *

from app import create_app
from app import config
from config import config



def send_email(recipient, subject, template, **kwargs):
    print("In send_mail")
    print("Recipient: %s"%recipient)

    app = create_app(os.getenv('FLASK_CONFIG') or 'default')
    with app.app_context():
        print("SENDER: %s" % app.config['ADMIN_EMAIL'])

        sg = sendgrid.SendGridAPIClient(apikey=app.config['MAIL_SENDGRID_API_KEY'])
        from_email = Email(app.config['ADMIN_EMAIL'])
        to_email = Email(recipient)
        subject = app.config['EMAIL_SUBJECT_PREFIX'] + ' ' + subject
        content = Content("text/html",render_template(template + '.html', **kwargs))
        mail = Mail(from_email, subject, to_email, content)
        
        response = sg.client.mail.send.post(request_body=mail.get())
        print("Status code: %s" %response.status_code)
        print("Body: %s" %response.body)
        print("Headers: %s" %response.headers)
