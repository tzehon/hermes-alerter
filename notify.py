import os

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from sendgrid.helpers.mail import To
from sendgrid.helpers.mail import Personalization

import config

def get_recipients():
    emails = config.get_emails()
    to_list = Personalization()

    for email in emails:
        to_list.add_to(To(email))
    return to_list
    
def email(wanted_bags, available_bags):
    print('Sending email')
    recipients = get_recipients()
    try:
        message = Mail(
            from_email='tth@example.com',
            subject='Latest Hermes selection',
            html_content='Wanted bags: ' + str(wanted_bags['categories']) + '\n' + 
                'Available bags:' + str(available_bags))
        message.add_personalization(recipients)
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        
        print(response.status_code)
        print(response.body)
        print(response.headers)
    
    except Exception as e:
        print(e)