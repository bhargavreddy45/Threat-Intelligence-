
print("SECURITY POLICY GOVERNANCE CHECKER")
print("-" * 42)

print("Paste your draft policy below.")
print("Type END on a separate line when finished.\n")

lines = []

while True:
    line = input()
    if line.strip().upper() == "END":
        break
    lines.append(line)

policy = " ".join(lines).lower()

requirements = {
    "Scope": ["scope", "applies to", "coverage"],
    "Roles and Responsibilities": [
        "roles and responsibilities", "responsibilities", "accountabilities"
    ],
    "Enforcement": ["enforcement", "disciplinary", "violations"],
    "Review Cycle": ["review cycle", "reviewed annually",
                     "review every", "annual review"],
    "Approval Authority": [
        "approval authority", "approved by", "authorized by"
    ]
}

missing = []

print("\nASSESSMENT RESULTS")
print("-" * 42)

for element, keywords in requirements.items():
    found = any(keyword in policy for keyword in keywords)

    if found:
        print(f"[PRESENT] {element}")
    else:
        print(f"[MISSING] {element}")
        missing.append(element)

print("\nSUMMARY")

if not missing:
    print("All five required elements were detected.")
else:
    print("Missing elements:", len(missing))
    for element in missing:
        print("-", element)

print("\nAssessment completed.")
