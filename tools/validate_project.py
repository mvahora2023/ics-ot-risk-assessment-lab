from pathlib import Path
from ipaddress import ip_address
import re
path=Path(__file__).resolve().parents[1]/"docs"/"asset-inventory.md"
text=path.read_text(encoding="utf-8")
assert "Simulated" in text and "fictional" in text.lower()
rows=[]
for line in text.splitlines():
    if re.match(r"^\|\s*AST-\d+\s*\|",line):
        rows.append([x.strip() for x in line.split("|")[1:-1]])
assert len(rows)>=10, "Too few lab assets"
assert all(len(row)==8 for row in rows), "Unexpected inventory schema"
for index in (0,1,5):
    values=[row[index] for row in rows]
    assert len(values)==len(set(values)),("Duplicate inventory identifier",index)
for row in rows:
    assert ip_address(row[5]).is_private,("Non-private training address",row[0])
    assert row[6] in ("High","Medium","Low","N/A (Assessment Tooling)")
print(f"Validated {len(rows)} synthetic ICS assets, unique IDs/names/addresses and criticalities.")
