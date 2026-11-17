# Q14 - SIEM Architecture Pipeline

from datetime import datetime


# -----------------------------
# 1. Collect Raw Events
# -----------------------------

def collect_events():
    events = [
        {
            "source": "Firewall",
            "message": "Failed login from 192.168.1.50"
        },
        {
            "source": "Windows",
            "message": "Failed login for administrator"
        },
        {
            "source": "IDS",
            "message": "Multiple login attempts detected from 192.168.1.50"
        },
        {
            "source": "Firewall",
            "message": "Connection blocked from 10.10.10.20"
        }
    ]

    return events


# -----------------------------
# 2. Normalize Events
# -----------------------------

def normalize_events(raw_events):
    normalized = []

    for event in raw_events:
        message = event["message"].lower()

        if "failed login" in message:
            event_type = "FAILED_LOGIN"
        elif "multiple login" in message:
            event_type = "BRUTE_FORCE"
        elif "blocked" in message:
            event_type = "BLOCKED_CONNECTION"
        else:
            event_type = "UNKNOWN"

        normalized_event = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "source": event["source"],
            "event_type": event_type,
            "message": event["message"]
        }

        normalized.append(normalized_event)

    return normalized


# -----------------------------
# 3. Correlate Events
# -----------------------------

def correlate_events(events):
    failed_logins = 0

    for event in events:
        if event["event_type"] in ["FAILED_LOGIN", "BRUTE_FORCE"]:
            failed_logins += 1

    return failed_logins


# -----------------------------
# 4. Raise Alert
# -----------------------------

def generate_alert(failed_logins):

    if failed_logins >= 2:
        return "ALERT: Possible brute-force attack detected!"

    return "No security alert generated."


# -----------------------------
# Main SIEM Pipeline
# -----------------------------

print("=" * 60)
print("SIEM END-TO-END PIPELINE")
print("=" * 60)

# Step 1
raw_events = collect_events()

print("\n1. RAW EVENTS")
for event in raw_events:
    print(event)


# Step 2
normalized_events = normalize_events(raw_events)

print("\n2. NORMALIZED EVENTS")
for event in normalized_events:
    print(event)


# Step 3
failed_logins = correlate_events(normalized_events)

print("\n3. CORRELATION")
print("Related authentication events:", failed_logins)


# Step 4
alert = generate_alert(failed_logins)

print("\n4. ALERT")
print(alert)

print("\nSIEM pipeline completed.")