controls = {
    "Organizational": ["policy", "supplier", "risk", "management"],
    "People": ["employee", "training", "awareness", "staff"],
    "Physical": ["door", "cctv", "building", "server room"],
    "Technological": ["firewall", "encryption", "malware", "network"]
}

description = input("Enter security control description: ").lower()

found = False

for domain, keywords in controls.items():
    for word in keywords:
        if word in description:
            print("ISO 27001 Domain:", domain)
            found = True
            break
    if found:
        break

if not found:
    print("Domain not identified")