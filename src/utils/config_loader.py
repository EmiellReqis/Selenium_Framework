import os
import yaml


def load_config():
    """
    Load the configuration from a YAML file.

    :return: Dictionary containing the configuration settings
    """
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.yaml')
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)
