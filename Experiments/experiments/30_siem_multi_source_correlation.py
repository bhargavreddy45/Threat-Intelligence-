"""Experiment 30: Correlate firewall, Windows, and VPN events for a brute-force case."""
FIREWALL_LOG = [
    {"src_ip": "198.51.100.25", "event": "connection_allowed"},
    {"src_ip": "198.51.100.25", "event": "repeated_auth_traffic"},
]
WINDOWS_LOG = [
    {"src_ip": "198.51.100.25", "account": "administrator", "event": "failed_login", "count": 5},
]
VPN_LOG = [
    {"src_ip": "198.51.100.25", "account": "administrator", "event": "vpn_success"},
]

def correlate(firewall, windows, vpn, minimum_failures=3):
    alerts = []
    for auth in windows:
        if auth["event"] != "failed_login" or auth["count"] < minimum_failures:
            continue
        same_ip_fw = any(e["src_ip"] == auth["src_ip"] and e["event"] == "repeated_auth_traffic" for e in firewall)
        same_ip_vpn = any(e["src_ip"] == auth["src_ip"] and e["event"] == "vpn_success"
                          and e["account"] == auth["account"] for e in vpn)
        if same_ip_fw and same_ip_vpn:
            alerts.append({"src_ip": auth["src_ip"], "account": auth["account"],
                           "failed_attempts": auth["count"],
                           "alert": "Correlated brute-force pattern followed by VPN success"})
    return alerts

if __name__ == "__main__":
    print("MULTI-SOURCE SIEM CORRELATION")
    print("Firewall events:", FIREWALL_LOG)
    print("Windows events:", WINDOWS_LOG)
    print("VPN events:", VPN_LOG)
    findings = correlate(FIREWALL_LOG, WINDOWS_LOG, VPN_LOG)
    print("\nCorrelation results:")
    for finding in findings:
        print("ALERT:", finding)
    if not findings:
        print("No correlated brute-force pattern detected.")
