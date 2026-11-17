
import re
from collections import Counter

# Raw log lines
logs = [
    "192.168.1.10 GET /home 200",
    "192.168.1.20 POST /login 401",
    "192.168.1.10 GET /home 200",
    "192.168.1.30 POST /login 403"
]

# Logstash-style parsing
def parse_log(line):
    pattern = r"(\S+)\s+(\S+)\s+(\S+)\s+(\d+)"
    match = re.match(pattern, line)

    if match:
        ip, method, path, status = match.groups()
        return {
            "ip": ip,
            "method": method,
            "path": path,
            "status": int(status)
        }

    return None

# Elasticsearch-style indexing
index = []

for log in logs:
    event = parse_log(log)
    if event:
        index.append(event)

print("Structured Events:")
for event in index:
    print(event)

# Kibana-style aggregation
status_counts = Counter(
    event["status"] for event in index
)

print("\nStatus Code Summary:")
for status, count in sorted(status_counts.items()):
    print(status, ":", count)

print("\nTotal logs indexed:", len(index))
