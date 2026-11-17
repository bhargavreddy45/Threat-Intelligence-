# Q16 - Defense-in-Depth Security Model

import random


class SecurityLayer:

    def __init__(self, name, protection_probability):
        self.name = name
        self.protection_probability = protection_probability

    def inspect(self):
        # Randomly determine whether this layer stops the attack
        result = random.random() < self.protection_probability
        return result


def simulate_attack(layers):

    print("=" * 60)
    print("DEFENSE-IN-DEPTH ATTACK SIMULATION")
    print("=" * 60)

    for layer in layers:

        print(f"\nTesting Layer: {layer.name}")

        stopped = layer.inspect()

        if stopped:
            print(f"RESULT: Attack BLOCKED by {layer.name}")
            return False
        else:
            print(f"RESULT: Attack bypassed {layer.name}")

    print("\nRESULT: Attack passed through ALL security layers!")
    return True


# Security layers
layers = [

    SecurityLayer(
        "Firewall",
        0.60
    ),

    SecurityLayer(
        "IDS/IPS",
        0.50
    ),

    SecurityLayer(
        "Endpoint Protection",
        0.70
    ),

    SecurityLayer(
        "Authentication / MFA",
        0.80
    ),

    SecurityLayer(
        "Application Security",
        0.60
    ),

    SecurityLayer(
        "Network Segmentation",
        0.50
    )
]


# Run simulation multiple times
successful_attacks = 0
total_simulations = 10

print(f"\nRunning {total_simulations} attack simulations...\n")

for i in range(1, total_simulations + 1):

    print(f"\n--- Simulation {i} ---")

    attack_successful = simulate_attack(layers)

    if attack_successful:
        successful_attacks += 1


print("\n" + "=" * 60)
print("FINAL RESULTS")
print("=" * 60)

blocked_attacks = total_simulations - successful_attacks

print("Total attacks:", total_simulations)
print("Attacks blocked:", blocked_attacks)
print("Attacks that passed all layers:", successful_attacks)

print("\nConclusion:")
print("Defense-in-Depth provides protection through multiple")
print("overlapping security controls rather than relying on one layer.")