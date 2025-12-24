import os
import yaml

def load_yaml_config(config_path):
    try:
        with open(config_path, 'r') as file:
            return yaml.safe_load(file)
    except yaml.YAMLError as e:
        raise ValueError(f"Failed to parse YAML config file: {e}")
    except FileNotFoundError:
        raise FileNotFoundError(f"Config file not found: {config_path}")

def get_environment_variable(var_name, default=None):
    return os.environ.get(var_name, default)

def validate_redis_config(config):
    for key in ['host', 'port', 'password']:
        if key not in config:
            raise ValueError(f"Missing required config key: {key}")
    return config

def validate_cache_config(config):
    for key in ['timeout', 'max_connections']:
        if key not in config:
            config[key] = 0
    return config