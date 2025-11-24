from colorama import Fore

def vuln_scan(target):
    print(Fore.YELLOW + "\n[+] Running Vulnerability Scanner...\n")

    vulns = []

    if target.startswith("http://"):
        print(Fore.RED + "[!] Website not using HTTPS (Security Risk)")
        vulns.append("No HTTPS")

    print(Fore.CYAN + f"\n[✔] Vulnerability Check Complete ({len(vulns)} alerts)")
    return vulns
