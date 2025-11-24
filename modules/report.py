import os

def save_report(data):
    if not os.path.exists("output"):
        os.mkdir("output")

    with open("output/report.txt", "w") as file:
        for section, result in data.items():
            file.write(f"\n=== {section} ===\n")
            for item in result:
                file.write(str(item) + "\n")

    print("\n[✔] Report saved at: output/report.txt")
