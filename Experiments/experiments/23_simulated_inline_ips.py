"""Experiment 23: Simulated inline IPS with a trusted-source whitelist.
This lab makes allow/block decisions on sample records; it does not block live traffic.
"""
SIGNATURES = [
    {"name": "SQL injection marker", "protocol": "TCP", "port": 80, "pattern": "UNION SELECT"},
    {"name": "Suspicious shell payload", "protocol": "TCP", "port": 443, "pattern": "/bin/sh"},
]
WHITELIST = {"192.0.2.10"}  # TEST-NET address reserved for documentation

TRAFFIC = [
    {"src": "198.51.100.20", "protocol": "TCP", "port": 80, "payload": "GET /?q=UNION SELECT"},
    {"src": "192.0.2.10", "protocol": "TCP", "port": 80, "payload": "GET /?q=UNION SELECT"},
    {"src": "198.51.100.30", "protocol": "TCP", "port": 22, "payload": "UNION SELECT"},
    {"src": "203.0.113.8", "protocol": "TCP", "port": 443, "payload": "POST /bin/sh"},
]

def inspect_packet(packet):
    if packet["src"] in WHITELIST:
        return "ALLOW (whitelisted trusted source)"
    for signature in SIGNATURES:
        if (packet["protocol"] == signature["protocol"]
                and packet["port"] == signature["port"]
                and signature["pattern"].lower() in packet["payload"].lower()):
            return "BLOCK (" + signature["name"] + ")"
    return "ALLOW (no signature match)"

if __name__ == "__main__":
    print("SIMULATED INLINE INTRUSION PREVENTION SYSTEM")
    print("Whitelist:", sorted(WHITELIST))
    for packet in TRAFFIC:
        print(packet, "=>", inspect_packet(packet))
