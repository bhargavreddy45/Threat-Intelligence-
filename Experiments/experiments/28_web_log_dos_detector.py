"""Experiment 28: Detect high request rates in timestamped web access logs."""
from collections import Counter
from datetime import datetime

LOGS = [
    "2026-11-16T10:00:01 198.51.100.7 GET /",
    "2026-11-16T10:00:05 198.51.100.7 GET /login",
    "2026-11-16T10:00:09 198.51.100.7 GET /search",
    "2026-11-16T10:00:12 198.51.100.7 GET /api",
    "2026-11-16T10:00:15 198.51.100.7 GET /products",
    "2026-11-16T10:00:20 203.0.113.4 GET /",
]

def detect_high_rate(lines, threshold=4):
    counts = Counter()
    for line in lines:
        parts = line.split()
        if len(parts) >= 2:
            try:
                datetime.fromisoformat(parts[0])
                counts[parts[1]] += 1
            except ValueError:
                continue
    return {ip: count for ip, count in counts.items() if count > threshold}, counts

if __name__ == "__main__":
    alerts, counts = detect_high_rate(LOGS, threshold=4)
    print("WEB SERVER POSSIBLE DoS DETECTOR")
    print("Requests per source IP:", dict(counts))
    print("Threshold: more than 4 requests in this sample window")
    if alerts:
        for ip, count in alerts.items():
            print(f"ALERT: {ip} generated {count} requests - investigate possible DoS")
    else:
        print("No source exceeded the configured threshold.")
