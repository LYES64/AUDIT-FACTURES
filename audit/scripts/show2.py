import json
d=json.load(open("all_data.json"))
def show(label,sh,n=999):
    print(f"\n===== {label} / {sh} =====")
    for i,r in enumerate(d[label][sh][:n]):
        print(i,"|".join(r))
for sh in ['F2026-16','F2026-20','F2026-22','F2026-24']:
    show("IRSH",sh)
