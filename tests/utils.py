import logging
import os
import yaml

logger = logging.getLogger(__name__)

def load_config(config_file):
    try:
        with open(config_file, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        logger.error(f"Config file {config_file} not found")
        return None
    except yaml.YAMLError as e:
        logger.error(f"Error parsing config file {config_file}: {e}")
        return None

def get_config_path():
    return os.environ.get('CACHE_REDIS_CONFIG_FILE', 'config.yaml')

def get_config():
    return load_config(get_config_path())