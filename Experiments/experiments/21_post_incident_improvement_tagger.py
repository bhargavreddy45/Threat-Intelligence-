"""Experiment 21: Tag improvement areas mentioned in a post-incident report."""
AREAS = {
    "Patch management": ["patch", "update", "unpatched", "vulnerability fix"],
    "Security awareness": ["awareness", "training", "phishing exercise", "user education"],
    "Monitoring": ["monitoring", "logging", "alert", "siem", "visibility"],
    "Backup strategy": ["backup", "restore", "recovery test", "offline copy"],
    "Access control": ["access control", "least privilege", "mfa", "permissions", "account review"]
}

def tag_report(report):
    text = report.lower()
    return [area for area, words in AREAS.items() if any(word in text for word in words)]

if __name__ == "__main__":
    report = ("The team will improve patch management, provide phishing awareness training, "
              "tune SIEM monitoring, test offline backups, and review least-privilege access.")
    print("POST-INCIDENT REPORT IMPROVEMENT TAGGER")
    print("Report:", report)
    tags = tag_report(report)
    print("Improvement areas identified:")
    for tag in tags:
        print("-", tag)
    if not tags:
        print("No listed improvement area detected.")
