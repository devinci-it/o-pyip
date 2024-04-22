"""
CLI tool for managing network interfaces.

This script provides a command-line interface (CLI) for managing network interfaces on a system. It allows users to list available network interfaces, set IP addresses for specific interfaces, and display help information.

Usage:
    python script_name.py [--interface INTERFACE] [--ip IP_ADDRESS] [--netmask NETMASK] [--list]

Options:
    --interface INTERFACE   Name of the interface.
    --ip IP_ADDRESS         IP address to set.
    --netmask NETMASK       Netmask to set.
    --list                  List available network interfaces.

"""

import argparse
import os
from tabulate import tabulate
from colorama import Fore, Style
from src.NetworkInterfaceManager import NetworkInterfaceManager



def clear_screen():
    """Clears the terminal screen."""
    os.system('clear')


def banner():
    """
    Generate a colored banner from the contents of the 'banner.txt' file.

    Reads the contents of the 'banner.txt' file, splits the text into two parts,
    and colorizes each part with green and blue colors. Returns the colored banner.

    Returns:
        str: The colored banner string.

    Raises:
        FileNotFoundError: If the 'banner.txt' file is not found.
    """
    try:
        with open("title.txt", "r") as file:
            banner_text = file.read()
            split_index = len(banner_text) // 2
            first_part = banner_text[:split_index]
            second_part = banner_text[split_index:]
            colored_banner = f"{Fore.YELLOW}{first_part}{Fore.BLUE}{second_part}{Style.RESET_ALL}"
            return colored_banner
    except FileNotFoundError:
        return "Error: The file 'banner.txt' was not found."

def print_banner():
    """Prints the banner."""
    print(banner())
def print_warning():
    """Prints the warning message if not running with sudo."""
    clear_screen()
    print(banner())
    print(f"{Fore.RED}-:{'-' * 80}:-{Style.RESET_ALL}")
    print(Fore.RED + "This script requires elevated privileges to access network interfaces.")
    print("Please run with 'sudo'." + Style.RESET_ALL)
    print(f"{Fore.RED}-:{'-' * 80}:-{Style.RESET_ALL}")

def print_interface_data(interface_data):
    """Prints the interface data in a colored table."""
    colored_table = tabulate(interface_data, headers=["Interface", "IP Address", "Netmask", "DNS Servers", "Default Gateway"])
    print(f"{Fore.GREEN}{colored_table}{Style.RESET_ALL}")

def parse_arguments():
    """Parses command-line arguments."""
    parser = argparse.ArgumentParser(description="pi: Manage network interfaces")
    parser.add_argument("--interface", help="Name of the interface")
    parser.add_argument("--ip", help="IP address to set")
    parser.add_argument("--netmask", help="Netmask to set")
    parser.add_argument("--list", action="store_true", help="List available network interfaces\n")
    return parser.parse_args()

def handle_list_action(interface_manager):
    """Handles the list action."""
    interface_data = interface_manager.retrieve_interface_data()
    print_interface_data(interface_data)

def handle_set_ip_address_action(interface_manager, interface, ip, netmask):
    """Handles setting IP address action."""
    interface_manager.set_ip_address(interface, ip, netmask)

def main():
    clear_screen()
    print_banner()

    if os.geteuid() != 0:
        print_warning()
        return

    parser = argparse.ArgumentParser(description="pi: Manage network interfaces")
    parser.add_argument("--interface", help="Name of the interface")
    parser.add_argument("--ip", help="IP address to set")
    parser.add_argument("--netmask", help="Netmask to set")
    parser.add_argument("--list", action="store_true", help="List available network interfaces\n")

    args = parser.parse_args()
    interface_manager = NetworkInterfaceManager()

    if args.list:
        handle_list_action(interface_manager)
    elif args.interface and args.ip and args.netmask:
        handle_set_ip_address_action(interface_manager, args.interface, args.ip, args.netmask)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
