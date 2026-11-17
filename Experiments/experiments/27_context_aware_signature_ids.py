"""Experiment 27: IDS alert requires both protocol/port context and content match."""
RULES = [
    {"name": "HTTP SQLi indicator", "protocol": "TCP", "port": 80, "pattern": "UNION SELECT"},
    {"name": "DNS tunneling marker", "protocol": "UDP", "port": 53, "pattern": "long-subdomain"},
]
PACKETS = [
    {"id": 1, "protocol": "TCP", "port": 80, "payload": "GET /?id=UNION SELECT"},
    {"id": 2, "protocol": "UDP", "port": 53, "payload": "long-subdomain"},
    {"id": 3, "protocol": "TCP", "port": 22, "payload": "UNION SELECT"},
    {"id": 4, "protocol": "TCP", "port": 80, "payload": "GET /home"},
]

def detect(packet):
    for rule in RULES:
        context_match = packet["protocol"] == rule["protocol"] and packet["port"] == rule["port"]
        content_match = rule["pattern"].lower() in packet["payload"].lower()
        if context_match and content_match:
            return "ALERT: " + rule["name"]
    return "No alert"

if __name__ == "__main__":
    print("CONTEXT-AWARE SIGNATURE IDS")
    for packet in PACKETS:
        print(f"Packet {packet['id']}: {detect(packet)}")
