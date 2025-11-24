import requests
from colorama import Fore

def subdomain_scan(target):
    print(Fore.YELLOW + "\n[+] Running Subdomain Enumeration...\n")

    wordlist = "wordlists/top.txt"
    found = []

    with open(wordlist, "r") as wl:
        for line in wl:
            sub = line.strip() + "." + target
            try:
                requests.get("http://" + sub, timeout=2)
                print(Fore.GREEN + "[FOUND] " + sub)
                found.append(sub)
            except:
                pass

    print(Fore.CYAN + f"\n[✔] Subdomain Scan Complete! ({len(found)} found)")
    return found
