"""Experiment 19: Simulate Splunk search filtering and stats count by field."""
from collections import Counter

EVENTS = [
    {"host": "web01", "sourcetype": "access", "status": 200, "user": "alice"},
    {"host": "web01", "sourcetype": "access", "status": 401, "user": "bob"},
    {"host": "vpn01", "sourcetype": "auth", "status": 401, "user": "bob"},
    {"host": "web02", "sourcetype": "access", "status": 500, "user": "carol"},
    {"host": "web02", "sourcetype": "access", "status": 401, "user": "alice"},
]

def search(events, field, value):
    return [event for event in events if str(event.get(field, "")).lower() == str(value).lower()]

def stats_count(events, field):
    return Counter(event.get(field, "UNKNOWN") for event in events)

if __name__ == "__main__":
    print("SIMULATED SPLUNK SEARCH AND STATS")
    filtered = search(EVENTS, "status", 401)
    print('\nSearch: status=401')
    for event in filtered:
        print(event)
    print("\nStats: count by sourcetype")
    for key, count in stats_count(EVENTS, "sourcetype").items():
        print(f"{key}: {count}")
