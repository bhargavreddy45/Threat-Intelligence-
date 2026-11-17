"""Experiment 17: Classify a security control into an ISO/IEC 27001:2022 Annex A domain."""
DOMAINS = {
    "Organizational": ["policy", "risk assessment", "supplier", "asset inventory", "incident management", "business continuity", "roles and responsibilities"],
    "People": ["training", "awareness", "background verification", "disciplinary", "employment", "remote working awareness"],
    "Physical": ["door", "building", "server room", "physical access", "cctv", "secure area", "equipment protection"],
    "Technological": ["firewall", "encryption", "multi-factor", "mfa", "logging", "malware", "endpoint", "network", "backup", "authentication", "access control"]
}

def classify_control(description):
    text = description.lower()
    scores = {domain: sum(1 for word in words if word in text) for domain, words in DOMAINS.items()}
    highest = max(scores.values())
    winners = [name for name, score in scores.items() if score == highest and score > 0]
    return (winners[0] if len(winners) == 1 else "Unclassified / Ambiguous"), scores

if __name__ == "__main__":
    print("ISO/IEC 27001:2022 ANNEX A DOMAIN CLASSIFIER")
    description = "The organization requires multi-factor authentication for remote access."
    result, scores = classify_control(description)
    print("Control description:", description)
    print("Domain scores:", scores)
    print("Classified domain:", result)
    print("Domains: Organizational, People, Physical, Technological")
