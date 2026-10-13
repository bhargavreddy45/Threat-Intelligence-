
print("THREAT INTELLIGENCE APPLICATION CLASSIFIER")
print("-" * 45)

scenario = input("Enter a business scenario: ").lower()

if any(word in scenario for word in
       ["bank", "banking", "payment", "credit card", "financial"]):
    result = "Banking Fraud Prevention"
    reason = "Detect suspicious transactions and financial fraud."

elif any(word in scenario for word in
         ["hospital", "healthcare", "patient", "medical", "clinic"]):
    result = "Healthcare Data Protection"
    reason = "Protect patient records and detect healthcare threats."

elif any(word in scenario for word in
         ["e-commerce", "ecommerce", "online shopping",
          "retail", "customer orders"]):
    result = "E-commerce Fraud Prevention"
    reason = "Detect fake orders, account abuse, and payment fraud."

elif any(word in scenario for word in
         ["school", "university", "college", "education"]):
    result = "Education Sector Security"
    reason = "Protect student records and institutional systems."

elif any(word in scenario for word in
         ["factory", "manufacturing", "industrial", "iot"]):
    result = "Industrial and IoT Security"
    reason = "Identify threats to connected devices and operations."

else:
    result = "General Cybersecurity"
    reason = "Identify threats, vulnerabilities, and suspicious activity."

print("\nRESULT")
print("Application Area:", result)
print("Reason:", reason)
