from colorama import Fore, Style, init
import datetime
import json
import os
import locale

init(autoreset=True)

USER_DATA_FILE = "user_data.json"

def load_user_data():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "r") as file:
            return json.load(file)
    return {}

def save_user_data(data):
    with open(USER_DATA_FILE, "w") as file:
        json.dump(data, file)

def get_username():
    user_data = load_user_data()
    if "name" not in user_data:
        name = input("[?] How do you want we call you? ")
        user_data["name"] = name
        save_user_data(user_data)
    return user_data["name"]

def print_welcome_message(name):
    locale.setlocale(locale.LC_TIME, 'en_US.utf8')
    current_date = datetime.datetime.now().strftime("%A %d %B %Y")
    print(f"{Fore.GREEN}Welcome {name}, we are the {current_date}")

def print_menu():
    print("\n[?] What do you want to do?")
    print(f"{Fore.YELLOW}1. Find an account")
    print(f"{Fore.YELLOW}2. Whois IP")
    print(f"{Fore.YELLOW}3. Scan ports")
    print(f"{Fore.YELLOW}4. Leave")
