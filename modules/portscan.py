import nmap
from colorama import Fore
import re

def clean_target(target):
    # Remove protocol http:// or https://
    target = re.sub(r'^https?://', '', target)
    # Remove trailing slashes
    return target.split('/')[0]

def port_scan(target):
    print(Fore.YELLOW + "\n[+] Running Port Scan...\n")

    target = clean_target(target)

    nm = nmap.PortScanner()

    try:
        nm.scan(target, '1-500')
    except Exception as e:
        print(Fore.RED + f"[ERROR] Nmap failed: {e}")
        return []

    open_ports = []

    if target not in nm.all_hosts():
        print(Fore.RED + f"[!] No response from target: {target}")
        return open_ports

    for port in nm[target]['tcp']:
        if nm[target]['tcp'][port]['state'] == 'open':
            print(Fore.GREEN + f"[OPEN] {port}")
            open_ports.append(port)

    print(Fore.CYAN + f"\n[✔] Port Scan Finished! ({len(open_ports)} open)")
    return open_ports
