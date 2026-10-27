# Q13 - Threat Intelligence Assessment

def assess_threat_intelligence(data):
    score = 0

    # Check for useful context
    context_keywords = [
        "campaign",
        "attacker",
        "malware",
        "target",
        "source",
        "indicator",
        "ioc",
        "infrastructure"
    ]

    # Check for confidence
    confidence_keywords = [
        "high confidence",
        "medium confidence",
        "low confidence",
        "confidence",
        "verified",
        "confirmed"
    ]

    # Check for actionability
    action_keywords = [
        "block",
        "monitor",
        "investigate",
        "isolate",
        "detect",
        "mitigate",
        "action",
        "recommended"
    ]

    data_lower = data.lower()

    has_context = any(word in data_lower for word in context_keywords)
    has_confidence = any(word in data_lower for word in confidence_keywords)
    has_actionability = any(word in data_lower for word in action_keywords)

    if has_context:
        score += 1

    if has_confidence:
        score += 1

    if has_actionability:
        score += 1

    print("\nThreat Intelligence Assessment")
    print("-" * 40)

    print("Context:", "Available" if has_context else "Missing")
    print("Confidence:", "Available" if has_confidence else "Missing")
    print("Actionability:", "Available" if has_actionability else "Missing")

    if score == 3:
        print("\nResult: GENUINE THREAT INTELLIGENCE")
        print("The information contains context, confidence, and actionable guidance.")

    elif score >= 1:
        print("\nResult: PARTIALLY PROCESSED INTELLIGENCE")
        print("The data contains some intelligence characteristics but needs more analysis.")

    else:
        print("\nResult: RAW DATA")
        print("The information has not yet been processed into useful threat intelligence.")


# Main program
data = input("Enter collected security data:\n")

assess_threat_intelligence(data)