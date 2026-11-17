"""Experiment 22: Detect repeated failed logins followed by success for one account."""
from collections import defaultdict

LOG_LINES = [
    "2026-11-16T09:00:01 user=alice status=FAIL",
    "2026-11-16T09:00:05 user=bob status=FAIL",
    "2026-11-16T09:00:09 user=alice status=FAIL",
    "2026-11-16T09:00:13 user=alice status=FAIL",
    "2026-11-16T09:00:20 user=alice status=SUCCESS",
]

def parse_line(line):
    fields = dict(item.split("=", 1) for item in line.split()[1:] if "=" in item)
    timestamp = line.split()[0]
    if "user" not in fields or "status" not in fields:
        return None
    return {"timestamp": timestamp, "user": fields["user"], "status": fields["status"].upper()}

def detect_pattern(lines, target_user, minimum_failures=3):
    failures = defaultdict(int)
    alerts = []
    for line in lines:
        event = parse_line(line)
        if not event or event["user"] != target_user:
            continue
        if event["status"] == "FAIL":
            failures[target_user] += 1
        elif event["status"] == "SUCCESS" and failures[target_user] >= minimum_failures:
            alerts.append((failures[target_user], event["timestamp"]))
            failures[target_user] = 0
    return alerts

if __name__ == "__main__":
    user = "alice"
    print("AUTHENTICATION BRUTE-FORCE PATTERN DETECTOR")
    for line in LOG_LINES:
        print(line)
    findings = detect_pattern(LOG_LINES, user)
    print(f"\nTarget account: {user}")
    if findings:
        for count, time in findings:
            print(f"ALERT: {count} failed logins followed by success at {time}")
    else:
        print("No matching pattern detected.")
