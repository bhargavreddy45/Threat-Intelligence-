# Q11 - Packet Sniffing using Scapy

from scapy.all import sniff


def display_packet(packet):
    print("=" * 60)
    print("Packet Captured")
    print("=" * 60)
    print(packet.summary())


print("Starting packet sniffing...")
print("Press Ctrl+C to stop.\n")

# Capture 10 packets
sniff(prn=display_packet, count=10)

print("\nPacket sniffing completed.")