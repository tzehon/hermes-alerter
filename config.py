import yaml

def load():
    with open(r'categories.yaml') as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        categories = yaml.load(file, Loader=yaml.FullLoader)
        # print(categories)
        return categories