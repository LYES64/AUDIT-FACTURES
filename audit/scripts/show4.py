import json
d=json.load(open("all_data.json"))
def show(label,sh,n=999):
    print(f"\n===== {label} / {sh} =====")
    for i,r in enumerate(d[label][sh][:n]):
        print(i,"|".join(r))
for sh in ['F2026-B01 ','F2026-B09','F2026-B10','F2026-B11','F2026-B12']:
    show("BARROS",sh)
