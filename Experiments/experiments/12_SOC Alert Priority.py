# Q12 - SOC Alert Priority Assignment

def assign_priority(alert):
    alert = alert.lower()

    # P1 - Critical
    if any(word in alert for word in [
        "ransomware",
        "data exfiltration",
        "active breach",
        "domain admin compromised",
        "critical server compromised"
    ]):
        return "P1 - Critical"

    # P2 - High
    elif any(word in alert for word in [
        "malware",
        "credential theft",
        "privilege escalation",
        "multiple failed logins",
        "suspicious powershell"
    ]):
        return "P2 - High"

    # P3 - Medium
    elif any(word in alert for word in [
        "port scan",
        "suspicious login",
        "phishing email",
        "unusual traffic"
    ]):
        return "P3 - Medium"

    # P4 - Low
    else:
        return "P4 - Low"


# Main program
print("SOC Alert Priority Classifier")
print("-" * 40)

alert = input("Enter SOC alert description: ")

priority = assign_priority(alert)

print("\nAlert:")
print(alert)

print("Assigned Priority:", priority)