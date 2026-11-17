
print("THREAT INTELLIGENCE REPORT CLASSIFIER")
print("-" * 45)

description = input("Enter report description: ").lower()
audience = input("Enter intended audience: ").lower()

strategic_words = [
    "business risk", "executive", "long-term", "geopolitical",
    "industry trends", "business impact", "senior management",
    "investment decision"
]

tactical_words = [
    "attack techniques", "tactics", "procedures", "ttp",
    "mitre", "attacker behavior", "attack patterns",
    "threat actor methods"
]

operational_words = [
    "incident", "active attack", "ip address", "ioc",
    "indicator of compromise", "malware hash", "alert",
    "malicious domain", "investigation"
]

strategic_audience = [
    "executive", "management", "board", "director", "business leader"
]

tactical_audience = [
    "security team", "threat hunter", "red team", "blue team"
]

operational_audience = [
    "soc analyst", "incident responder", "incident response",
    "forensic analyst", "security analyst"
]


def count_matches(text, keywords):
    return sum(1 for word in keywords if word in text)


scores = {
    "Strategic": (
        count_matches(description, strategic_words)
        + count_matches(audience, strategic_audience)
    ),
    "Tactical": (
        count_matches(description, tactical_words)
        + count_matches(audience, tactical_audience)
    ),
    "Operational": (
        count_matches(description, operational_words)
        + count_matches(audience, operational_audience)
    )
}

print("\nCLASSIFICATION RESULTS")
for category, score in scores.items():
    print(f"{category}: {score} matching indicators")

highest = max(scores.values())
winners = [name for name, score in scores.items() if score == highest]

if highest == 0:
    result = "Unclassified"
elif len(winners) > 1:
    result = "Ambiguous: " + ", ".join(winners)
else:
    result = winners[0]

print("\nReport classification:", result)
print("Note: This is a keyword-based educational classifier.")
