import json,re,sys
for f,label in [("/root/.claude/projects/-home-user-AUDIT-FACTURES/7767e6b5-de9b-5631-a5c3-b77beef4874c/tool-results/mcp-Gmail-get_thread-1783608798837.txt","F16-24 SENDING"),
                ("/root/.claude/projects/-home-user-AUDIT-FACTURES/7767e6b5-de9b-5631-a5c3-b77beef4874c/tool-results/mcp-Gmail-get_thread-1783608799859.txt","FACTURES RESTANTES 09/07")]:
    d=json.load(open(f))
    print("\n\n############",label,"— ",len(d["messages"]),"messages")
    for m in d["messages"]:
        body=m.get("plaintextBody") or m.get("plainTextBody") or m.get("plaintext_body") or ""
        # find keys
        if not body:
            for k in m:
                if 'lain' in k.lower() and isinstance(m[k],str): body=m[k]
        body=re.sub(r'\n{3,}','\n',body).strip()
        # trim signature/quoted
        print("\n----",m.get("date","?"),"|",m.get("sender","?"),"|",m.get("subject","")[:60])
        print(body[:1400])
