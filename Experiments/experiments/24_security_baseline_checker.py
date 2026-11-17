"""Experiment 24: Compare current security settings with a minimum baseline."""
BASELINE = {
    "mfa_enabled": True,
    "disk_encryption": True,
    "endpoint_protection": True,
    "critical_patching_days": 14,
    "backup_frequency_hours": 24,
    "logging_enabled": True,
}
CURRENT = {
    "mfa_enabled": True,
    "disk_encryption": False,
    "endpoint_protection": True,
    "critical_patching_days": 30,
    "backup_frequency_hours": 48,
    "logging_enabled": True,
}

def check_baseline(baseline, current):
    failures = []
    for control, minimum in baseline.items():
        actual = current.get(control)
        if actual is None:
            failures.append((control, "NOT CONFIGURED", minimum))
        elif isinstance(minimum, bool) and actual != minimum:
            failures.append((control, actual, minimum))
        elif isinstance(minimum, (int, float)) and actual > minimum:
            failures.append((control, actual, minimum))
    return failures

if __name__ == "__main__":
    print("SECURITY CONTROL BASELINE CHECK")
    for key, value in CURRENT.items():
        print(f"{key}: {value}")
    failures = check_baseline(BASELINE, CURRENT)
    print("\nControls failing the minimum baseline:")
    if failures:
        for control, actual, required in failures:
            print(f"- {control}: current={actual}; required={required}")
    else:
        print("None. All checked controls meet the baseline.")
