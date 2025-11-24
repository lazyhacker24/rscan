from modules.banner import banner
from modules.subdomain_enum import subdomain_scan
from modules.dir_enum import dir_enum
from modules.portscan import port_scan
from modules.vulnscan import vuln_scan
from modules.report import save_report

def main():
    banner()
    print("""
[1] Subdomain Scan
[2] Directory Bruteforce
[3] Port Scan
[4] Vulnerability Scan
[5] Full Scan
[6] Exit
    """)

    choice = input("Select option: ")
    if choice == "6":
        quit()

    target = input("Enter target URL/IP: ")

    results = {}

    if choice in ["1", "5"]:
        results["Subdomains"] = subdomain_scan(target)

    if choice in ["2", "5"]:
        results["Directories"] = dir_enum(target)

    if choice in ["3", "5"]:
        results["Open Ports"] = port_scan(target)

    if choice in ["4", "5"]:
        results["Vulnerabilities"] = vuln_scan(target)

    save_report(results)

if __name__ == "__main__":
    main()
