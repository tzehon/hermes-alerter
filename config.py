import os
import yaml

def get_emails():
    emails = os.environ.get('EMAILS').split()
    return emails

def load():
    with open(r'categories.yaml') as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        categories = yaml.load(file, Loader=yaml.FullLoader)
        # print(categories)
        return categories