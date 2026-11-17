"""Experiment 20: Keyword-based network threat classifier."""
CATEGORIES = {
    "Phishing": ["fake login", "credential", "deceptive email", "malicious link", "spoofed email"],
    "DoS/DDoS": ["traffic flood", "overwhelmed", "service unavailable", "denial of service", "many requests"],
    "Malware": ["ransomware", "trojan", "malicious file", "virus", "payload"],
    "Man-in-the-Middle": ["intercept", "altered in transit", "rogue access point", "session hijack", "between client and server"]
}

def classify(description):
    text = description.lower()
    scores = {name: sum(term in text for term in terms) for name, terms in CATEGORIES.items()}
    best = max(scores.values())
    winners = [name for name, score in scores.items() if score == best and score > 0]
    return (winners[0] if len(winners) == 1 else "Unknown / Ambiguous"), scores

if __name__ == "__main__":
    incident = "A traffic flood made the public service unavailable."
    result, scores = classify(incident)
    print("NETWORK THREAT CATEGORY CLASSIFIER")
    print("Incident:", incident)
    print("Scores:", scores)
    print("Detected category:", result)
