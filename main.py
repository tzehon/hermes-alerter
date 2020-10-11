import requests
import pprint
import os

from flask import Flask
from bs4 import BeautifulSoup

import config
import notify

app = Flask(__name__)

@app.route('/')
def hermes_scraper():
    wanted_bags = config.load()
    print(wanted_bags['categories'])

    URL = 'https://www.hermes.com/sg/en/category/women/bags-and-small-leather-goods/bags-and-clutches/'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    bags_on_site = soup.find_all(class_='product-item-name')
    available_bags = []

    for bag_on_site_html in bags_on_site:
        bag_on_site = bag_on_site_html.text.strip()
        for wanted_bag in wanted_bags['categories']:
            print("Bag on site: " + bag_on_site)
            print("Wanted: " + wanted_bag + "\n")

            if wanted_bag in bag_on_site:
                available_bags.append(bag_on_site)

    print("Wanted bags: " + str(wanted_bag))
    print("Available bags: " + str(available_bags))
    notify.email(wanted_bags, available_bags)
    return str(available_bags)

    if __name__ == "__main__":
        app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))