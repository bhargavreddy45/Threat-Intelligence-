# Q15 - Security Incident Root-Cause Classification

def classify_incident(narrative):

    text = narrative.lower()

    scores = {
        "Phishing": 0,
        "Unpatched Vulnerability": 0,
        "Misconfiguration": 0,
        "Insider Threat": 0,
        "Supply-Chain Compromise": 0
    }

    # Phishing indicators
    phishing_words = [
        "phishing",
        "fake email",
        "malicious email",
        "credential",
        "link",
        "attachment",
        "spoofed"
    ]

    # Vulnerability indicators
    vulnerability_words = [
        "unpatched",
        "vulnerability",
        "security patch",
        "exploit",
        "outdated software",
        "cve"
    ]

    # Misconfiguration indicators
    misconfiguration_words = [
        "misconfiguration",
        "incorrect configuration",
        "open port",
        "publicly exposed",
        "access control",
        "permissions"
    ]

    # Insider threat indicators
    insider_words = [
        "insider",
        "employee",
        "employee stole",
        "disgruntled employee",
        "unauthorized employee",
        "internal user"
    ]

    # Supply-chain indicators
    supply_chain_words = [
        "third party",
        "vendor",
        "supplier",
        "software update",
        "dependency",
        "supply chain",
        "compromised vendor"
    ]

    for word in phishing_words:
        if word in text:
            scores["Phishing"] += 1

    for word in vulnerability_words:
        if word in text:
            scores["Unpatched Vulnerability"] += 1

    for word in misconfiguration_words:
        if word in text:
            scores["Misconfiguration"] += 1

    for word in insider_words:
        if word in text:
            scores["Insider Threat"] += 1

    for word in supply_chain_words:
        if word in text:
            scores["Supply-Chain Compromise"] += 1

    # Find highest score
    category = max(scores, key=scores.get)

    if scores[category] == 0:
        category = "Unknown"

    return category, scores


# Main program
print("Security Incident Root-Cause Classifier")
print("-" * 50)

narrative = input("Enter the security incident case study:\n")

category, scores = classify_incident(narrative)

print("\nClassification Results")
print("-" * 50)

for key, value in scores.items():
    print(f"{key}: {value}")

print("\nMost Likely Root Cause:")
print(category)