
def encrypt(data, key):
    data_bytes = data.encode("utf-8")
    key_bytes = key.encode("utf-8")

    encrypted = bytes(
        byte ^ key_bytes[i % len(key_bytes)]
        for i, byte in enumerate(data_bytes)
    )

    return encrypted


def decrypt(encrypted, key):
    key_bytes = key.encode("utf-8")

    decrypted = bytes(
        byte ^ key_bytes[i % len(key_bytes)]
        for i, byte in enumerate(encrypted)
    )

    return decrypted.decode("utf-8", errors="replace")


print("VPN CONFIDENTIALITY DEMONSTRATION")
print("-" * 42)

message = input("Enter a message to send: ")
key = input("Enter a shared key: ")

if not message or not key:
    print("Error: Message and key must not be empty.")
    raise SystemExit

ciphertext = encrypt(message, key)

print("\nOriginal message:", message)
print("Captured transit data (hex):", ciphertext.hex())
print("Without decryption, the data is not readable as plaintext.")

recovered = decrypt(ciphertext, key)
print("\nAfter decryption with the shared key:", recovered)

print("\nConfidentiality demonstration completed.")
print("WARNING: XOR is not secure VPN encryption.")
