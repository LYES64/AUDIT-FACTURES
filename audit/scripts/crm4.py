import json
from collections import Counter
rows=json.load(open("crm_rows.json"))
data=rows[2:]  # skip title+header
hdr=rows[1]
print("STATUTS:",Counter(r[5] for r in data if len(r)>5))
print("TYPES:",Counter(r[1] for r in data if len(r)>1))
print("\nTOUTES LES LIGNES CRM (",len(data),"):")
for r in data:
    r=(r+[""]*10)[:10]
    print(f"{r[0]:12}|{r[1]:5}|{r[4]:11}|{r[5]:18}|{r[6][:28]:28}|{r[7]:6}|{r[9]}")
