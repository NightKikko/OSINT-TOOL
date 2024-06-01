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
    print(f"{Fore.CYAN}Scan IP address from port {start_port} to {end_port}")
    for port in range(start_port, end_port + 1):
        if scan_port(host, port):
            print(f"{Fore.GREEN}Port {port} is open.")
        else:
            print(f"{Fore.RED}port {port} is close.")

if __name__ == "__main__":
    host = input("Enter IP Adress: ")
    start_port = int(input("Enter the departure port: "))
    end_port = int(input("Enter the arrival port: "))
    scan_ports(host, start_port, end_port)
