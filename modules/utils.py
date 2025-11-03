import json
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)
