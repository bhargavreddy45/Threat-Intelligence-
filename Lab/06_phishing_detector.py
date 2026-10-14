
from urllib.parse import urlparse
import ipaddress

def detect_phishing(url):
    score = 0
    reasons = []

    parsed = urlparse(url if "://" in url else "http://" + url)
    domain = parsed.hostname or ""

    keywords = ["login", "verify", "update", "password",
                "banking", "secure", "account"]

    if any(word in url.lower() for word in keywords):
        score += 1
        reasons.append("Suspicious keyword found")

    try:
        ipaddress.ip_address(domain)
        score += 1
        reasons.append("IP address used as domain")
    except ValueError:
        pass

    if len(domain.split(".")) > 4:
        score += 1
        reasons.append("Excessive subdomains")

    if parsed.scheme == "http":
        score += 1
        reasons.append("Uses HTTP instead of HTTPS")

    if score >= 2:
        print("Warning: Suspicious URL detected!")
    else:
        print("No major phishing indicators detected.")

    print("Risk score:", score)
    for reason in reasons:
        print("-", reason)


url = input("Enter a URL: ")
detect_phishing(url)
