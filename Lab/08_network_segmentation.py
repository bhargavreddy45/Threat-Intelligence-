
# Define network segments
segments = {
    "Guest": 1,
    "Employee": 2,
    "Sensitive": 3
}

# Access policy
allowed_access = {
    "Guest": ["Guest"],
    "Employee": ["Employee", "Guest"],
    "Sensitive": ["Sensitive", "Employee"]
}

def check_access(source, destination):
    print(f"{source} -> {destination}")

    if destination in allowed_access[source]:
        print("Access ALLOWED\n")
    else:
        print("Access BLOCKED by segmentation policy\n")

# Simulate network traffic
check_access("Guest", "Guest")
check_access("Guest", "Sensitive")
check_access("Employee", "Sensitive")
check_access("Sensitive", "Employee")
