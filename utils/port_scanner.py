import socket
from colorama import Fore, Style, init

init(autoreset=True)

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            return True
        else:
            return False
    except Exception as e:
        print(f"{Fore.RED}Erreur ! {e}")
        return False 
    finally:
        sock.close()

def scan_ports(host, start_port, end_port):
    print(f"{Fore.CYAN}Scan de l'adresse ip du port {start_port} à {end_port}")
    for port in range(start_port, end_port + 1):
        if scan_port(host, port):
            print(f"{Fore.GREEN}Le port {port} est ouvert.")
        else:
            print(f"{Fore.RED}Le port {port} est fermé.")

if __name__ == "__main__":
    host = input("Entrez l'ip à chercher: ")
    start_port = int(input("Entrez le port de départ: "))
    end_port = int(input("Entrez le port d'arrivée: "))
    scan_ports(host, start_port, end_port)
