import requests
import json
from termcolor import colored
import pyfiglet

# 
def banner():
    ascii_banner = pyfiglet.figlet_format("TeamBdCyberNinja", font="slant")
    print(colored(ascii_banner, 'cyan'))
    print(colored("Tool by TeamBdCyberNinja/CyberXploitBd", 'green'))
    print(colored("IP Address Information Gathering Tool\n", 'yellow'))

# IP 
def get_ip_info(ip_address):
    try:
        response = requests.get(f"http://ipinfo.io/{ip_address}/json")
        data = response.json()

        if "bogon" in data:
            print(colored(f"\nInvalid IP or Private Network Detected!", 'red'))
            return

        print(colored(f"\nInformation for IP: {ip_address}\n", 'blue'))
        print(colored(f"IP: {data.get('ip')}", 'green'))
        print(colored(f"City: {data.get('city')}", 'green'))
        print(colored(f"Region: {data.get('region')}", 'green'))
        print(colored(f"Country: {data.get('country')}", 'green'))
        print(colored(f"Location (Lat/Lon): {data.get('loc')}", 'green'))
        print(colored(f"Organization: {data.get('org')}", 'green'))
        print(colored(f"Timezone: {data.get('timezone')}", 'green'))
        print(colored(f"Postal: {data.get('postal')}\n", 'green'))

    except Exception as e:
        print(colored(f"Error: {str(e)}", 'red'))


def main():
    banner()
    ip_address = input(colored("Enter the IP address you want to track: ", 'yellow'))
    get_ip_info(ip_address)

if __name__ == "__main__":
    main()
                          
