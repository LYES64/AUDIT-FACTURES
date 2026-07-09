import json,re
d=json.load(open("/root/.claude/projects/-home-user-AUDIT-FACTURES/7767e6b5-de9b-5631-a5c3-b77beef4874c/tool-results/mcp-Gmail-get_thread-1783608799859.txt"))
msgs=d["messages"]
# print only the two most recent messages full text
for m in msgs[-2:]:
    body=""
    for k in m:
        if 'lain' in k.lower() and isinstance(m[k],str): body=m[k]
    body=re.sub(r'\n{2,}','\n',body).strip()
    print("\n----",m.get("date"),"|",m.get("sender"),"|",m.get("subject","")[:50])
    # cut quoted history
    body=re.split(r'\nDe :|\nLe .* a écrit|\n>',body)[0]
    print(body[:2500])
