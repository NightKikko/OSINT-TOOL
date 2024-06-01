import asyncio

from colorama import Fore, Style, init
from utils.welcome import *
from utils.ascii_art import *
from utils.username_search import *
from utils.ip_search import *
from utils.port_scanner import *

def main():
    name = get_username()
    print_welcome_message(name)

    while True:
        print_ascii_art()
        print_menu()
        choice = input(f"{Fore.BLUE}Enter your choice: {Style.RESET_ALL}")

        if choice == '1':
            username = input("$ Enter the username to search: ")
            asyncio.run(search_username(username))
        elif choice == '2':
            asyncio.run(search_ip())
        elif choice == '3':
            host = input("$ Enter the host to scan: ")
            start_port = int(input("$ Enter the starting port: "))
            end_port = int(input("$ Enter the ending port: "))
            asyncio.run(scan_ports(host, start_port, end_port))
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print(f"{Fore.RED}[!] Invalid choice, please try again.")

if __name__ == "__main__":
    main()
