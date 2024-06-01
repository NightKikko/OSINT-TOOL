import asyncio
from colorama import Fore, Style, init
from utils.utils import print_welcome_message, print_menu, get_username, print_ascii_art
from utils.username_search import search_username
from utils.ip_search import search_ip
from utils.port_scanner import scan_ports
import datetime
import json
import os
import locale

init(autoreset=True)  # Initialize colorama

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
        name = input("What would you like us to call you?: ")
        user_data["name"] = name
        save_user_data(user_data)
    return user_data["name"]

def print_welcome_message(name):
    locale.setlocale(locale.LC_TIME, 'en_US.utf8')
    current_date = datetime.datetime.now().strftime("%A %d %B %Y")
    print(f"{Fore.GREEN}Welcome {name}, today is {current_date}")

def print_menu():
    print("\nWhat would you like to do?")
    print(f"{Fore.YELLOW}1. Find an account")
    print(f"{Fore.YELLOW}2. Find an IP")
    print(f"{Fore.YELLOW}3. Scan ports")
    print(f"{Fore.YELLOW}4. Quit")

def main():
    print_ascii_art()
    name = get_username()
    print_welcome_message(name)

    while True:
        print_menu()
        choice = input(f"{Fore.BLUE}Enter your choice: {Style.RESET_ALL}")

        if choice == '1':
            username = input("Enter the username to search: ")
            asyncio.run(search_username(username))
        elif choice == '2':
            ip = input("Enter the IP address to search: ")
            search_ip(ip)
        elif choice == '3':
            host = input("Enter the host to scan: ")
            start_port = int(input("Enter the starting port: "))
            end_port = int(input("Enter the ending port: "))
            scan_ports(host, start_port, end_port)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print(f"{Fore.RED}Invalid choice, please try again.")

if __name__ == "__main__":
    main()

def print_ascii_art():
    ascii_art = """
   ____      _       _   
  / __ \\    (_)     | |  
 | |  | |___ _ _ __ | |_ 
 | |  | / __| | '_ \\| __|
 | |__| \\__ \\ | | | | |_ 
  \\____/|___/_|_| |_|\\__|
                         
    """
    print(Fore.CYAN + ascii_art)
