import requests
import pprint
from bs4 import BeautifulSoup

wanted_bags = [
    'Lindy',
    'Birkin',
    'Kelly',
    'Bolide 27'
]

URL = 'https://www.hermes.com/sg/en/category/women/bags-and-small-leather-goods/bags-and-clutches/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

items = soup.find_all(class_='product-item-name')

interested_bags = []
for item in items:
    available_bag = item.text.strip()
    for wanted_bag in wanted_bags:
        if wanted_bag in available_bag:
            interested_bags.append(available_bag)

print("Interested bags: " + str(wanted_bags))
print("Available bags: " + str(interested_bags))