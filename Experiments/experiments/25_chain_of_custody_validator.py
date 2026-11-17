"""Experiment 25: Validate evidence hash links and non-decreasing timestamps."""
import hashlib

def record_hash(record_id, timestamp, evidence, previous_hash):
    payload = f"{record_id}|{timestamp}|{evidence}|{previous_hash}".encode()
    return hashlib.sha256(payload).hexdigest()

def build_sample_chain():
    records = []
    previous = "GENESIS"
    for rid, stamp, evidence in [
        ("E001", "2026-11-16T09:00:00", "disk_image.dd"),
        ("E002", "2026-11-16T09:15:00", "sealed_usb"),
        ("E003", "2026-11-16T09:30:00", "evidence_bag_03"),
    ]:
        digest = record_hash(rid, stamp, evidence, previous)
        records.append({"id": rid, "timestamp": stamp, "evidence": evidence,
                        "previous_hash": previous, "hash": digest})
        previous = digest
    return records

def validate_chain(records):
    previous_hash = "GENESIS"
    previous_time = None
    issues = []
    for record in records:
        if record["previous_hash"] != previous_hash:
            issues.append(f"{record['id']}: previous hash link is broken")
        expected = record_hash(record["id"], record["timestamp"],
                                record["evidence"], record["previous_hash"])
        if record["hash"] != expected:
            issues.append(f"{record['id']}: record hash does not match")
        if previous_time and record["timestamp"] < previous_time:
            issues.append(f"{record['id']}: timestamp moved backwards")
        previous_time = record["timestamp"]
        previous_hash = record["hash"]
    return issues

if __name__ == "__main__":
    chain = build_sample_chain()
    print("CHAIN-OF-CUSTODY VALIDATOR")
    for record in chain:
        print(record)
    issues = validate_chain(chain)
    print("\nRESULT:", "VALID - unbroken hash and timestamp chain" if not issues else "INVALID")
    for issue in issues:
        print("-", issue)
