import requests
from colorama import Fore

def dir_enum(target):
    print(Fore.YELLOW + "\n[+] Running Directory Bruteforce...\n")

    wordlist = "wordlists/top.txt"
    found = []

    with open(wordlist, "r") as wl:
        for line in wl:
            path = target.rstrip("/") + "/" + line.strip()
            try:
                r = requests.get(path, timeout=2)
                if r.status_code in [200, 403]:
                    print(Fore.GREEN + "[FOUND] " + path)
                    found.append(path)
            except:
                pass

    print(Fore.CYAN + f"\n[✔] Directory Scan Done! ({len(found)} found)")
    return found
