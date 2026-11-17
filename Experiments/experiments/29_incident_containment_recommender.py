"""Experiment 29: Recommend containment for a described security incident."""
STRATEGIES = {
    "Ransomware": ["ransomware", "files encrypted", "encryption of files"],
    "Compromised account": ["stolen password", "account compromised", "credential theft", "unauthorized login"],
    "Malware infection": ["malware", "trojan", "infected endpoint", "malicious executable"],
    "DoS/DDoS": ["traffic flood", "denial of service", "ddos", "service overwhelmed"],
    "Data exfiltration": ["data exfiltration", "data stolen", "unauthorized data transfer"]
}
ACTIONS = {
    "Ransomware": "Isolate affected endpoints from the network; preserve evidence; activate recovery procedures.",
    "Compromised account": "Disable or suspend the account; revoke sessions/tokens; reset credentials and enforce MFA.",
    "Malware infection": "Quarantine the affected host; preserve a forensic image; scan related endpoints.",
    "DoS/DDoS": "Apply approved upstream rate limiting/scrubbing and coordinate with the ISP or hosting provider.",
    "Data exfiltration": "Restrict suspected outbound paths; protect affected data stores; preserve network and access logs."
}

def recommend(description):
    text = description.lower()
    scores = {name: sum(term in text for term in terms) for name, terms in STRATEGIES.items()}
    best = max(scores.values())
    winners = [name for name, score in scores.items() if score == best and score > 0]
    if len(winners) != 1:
        return "Manual triage required", "Escalate to the incident-response lead; preserve logs and validate the scope."
    category = winners[0]
    return category, ACTIONS[category]

if __name__ == "__main__":
    incident = "Several workstations show ransomware and files encrypted."
    category, action = recommend(incident)
    print("INCIDENT CONTAINMENT RECOMMENDER")
    print("Incident:", incident)
    print("Category:", category)
    print("Recommended containment:", action)
    print("Confirm actions against your incident-response plan before execution.")
