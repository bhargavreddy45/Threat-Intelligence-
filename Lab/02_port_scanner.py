
import socket

print("SIMPLE TCP PORT SCANNER")
print("-" * 35)

target = input("Enter target IP or hostname (default 127.0.0.1): ").strip()

if not target:
    target = "127.0.0.1"

ports_input = input(
    "Enter ports separated by commas (default 22,80,443,8080): "
).strip()

if ports_input:
    try:
        ports = sorted(set(int(p.strip()) for p in ports_input.split(",")))
        if any(port < 1 or port > 65535 for port in ports):
            raise ValueError("Ports must be between 1 and 65535.")
    except ValueError as error:
        print("Invalid port input:", error)
        raise SystemExit
else:
    ports = [22, 80, 443, 8080]

print("\nTarget:", target)
print("Scanning selected TCP ports...\n")

try:
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))

            if result == 0:
                print(f"Port {port}: OPEN")
            else:
                print(f"Port {port}: CLOSED or FILTERED")

except socket.gaierror:
    print("Error: Hostname could not be resolved.")
except OSError as error:
    print("Network error:", error)

print("\nScan completed.")
