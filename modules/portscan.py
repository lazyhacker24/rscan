import nmap
from colorama import Fore

def port_scan(target):
    print(Fore.YELLOW + "\n[+] Running Port Scan...\n")

    nm = nmap.PortScanner()
    nm.scan(target, '1-500')

    open_ports = []

    for port in nm[target]['tcp']:
        if nm[target]['tcp'][port]['state'] == 'open':
            print(Fore.GREEN + f"[OPEN] {port}")
            open_ports.append(port)

    print(Fore.CYAN + f"\n[✔] Port Scan Finished! ({len(open_ports)} open)")
    return open_ports
