# Placeholder for config_loader.py
import yaml

def load_config(file_path: str = "config.yaml"):
    with open(file_path, "r") as file:
        return yaml.safe_load(file)