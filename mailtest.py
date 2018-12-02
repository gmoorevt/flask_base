import sendgrid
import os
from sendgrid.helpers.mail import *

print("loading apikey")
sg = sendgrid.SendGridAPIClient(apikey='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')
print(sg)

from_email = Email("geody.moore@gmail.com")
to_email = Email("geody.moore@gmail.com")
subject = "My second email"
content = Content("text/plain", "and easy to do anywhere, even with Python this is it Geody")
mail = Mail(from_email, subject, to_email, content)
print(mail)
response = sg.client.mail.send.post(request_body=mail.get())

print("+++++++++++++++++++++++++")
print(response.status_code)
print(response.body)
print(response.headers)