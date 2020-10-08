import requests
import pprint
import os

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from flask import Flask
from bs4 import BeautifulSoup

import config

app = Flask(__name__)

@app.route('/')
def hermes_scraper():
    bags = config.load()
    print(bags['categories'])

    URL = 'https://www.hermes.com/sg/en/category/women/bags-and-small-leather-goods/bags-and-clutches/'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    items = soup.find_all(class_='product-item-name')

    interested_bags = []
    for item in items:
        available_bag = item.text.strip()
        for wanted_bag in bags['categories']:
            print("Bag on site: " + available_bag)
            print("Wanted: " + wanted_bag + "\n")

            if wanted_bag in available_bag:
                interested_bags.append(available_bag)

    print("Available bags: " + str(interested_bags))

    try:
        message = Mail(
            from_email='tth@example.com',
            to_emails='staceywongss@gmail.com',
            subject='Latest Hermes selection',
            html_content='Wanted bags: ' + str(categories) + '\n' + 
                'Available bags:' + str(interested_bags))

        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)

    return str(interested_bags)

    if __name__ == "__main__":
        app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))