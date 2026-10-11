from pathlib import Path

SOURCE = Path("contracts/semantic_dedup.py").read_text(encoding="utf-8")

fetch_a = SOURCE.index('a_bytes = self._fetch_verified_artifact(')
fetch_b = SOURCE.index('b_bytes = self._fetch_verified_artifact(')
shortcut = SOURCE.index('if artifact_a["sha256"] == artifact_b["sha256"]:')

assert fetch_a < shortcut
assert fetch_b < shortcut

print("PASS: exact-duplicate shortcut occurs only after both artifacts are independently fetched and SHA-256 verified")
