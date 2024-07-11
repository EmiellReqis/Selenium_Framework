import os
import yaml


def load_locators(site_name, page_name):
    """
    Load the locators for a given site and page from a YAML file.

    :param site_name: Name of the site
    :param page_name: Name of the page
    :return: Dictionary containing the locators for the specified page
    """
    locators_path = os.path.join(os.path.dirname(__file__), '..', 'locators', site_name, f'{page_name}.yaml')
    with open(locators_path, 'r') as file:
        return yaml.safe_load(file)

# Usage example
# locators = load_locators('saucedemo', 'home_page')
# print(locators)
