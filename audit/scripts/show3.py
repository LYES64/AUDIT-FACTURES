import json
d=json.load(open("all_data.json"))
def show(label,sh,n=999):
    print(f"\n===== {label} / {sh} =====")
    for i,r in enumerate(d[label][sh][:n]):
        print(i,"|".join(r))
show("BARROS","Suivi Factures")
show("BARROS","Copy")
