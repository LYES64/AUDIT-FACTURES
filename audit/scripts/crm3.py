import zipfile,json
from xml.etree import ElementTree as ET
f="/root/.claude/uploads/7767e6b5-de9b-5631-a5c3-b77beef4874c/ae2485a5-Compiexe__Ind_pendance_Royale_S_nior_Habitat_1.xlsx"
z=zipfile.ZipFile(f)
ns='{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
t=ET.fromstring(z.read('xl/worksheets/sheet1.xml'))
def colnum(ref):
    import re
    letters=re.match(r'[A-Z]+',ref).group()
    n=0
    for c in letters: n=n*26+(ord(c)-64)
    return n-1
rows=[]
for row in t.findall(ns+'sheetData/'+ns+'row'):
    cells={}
    maxc=0
    for c in row.findall(ns+'c'):
        ref=c.get('r'); ci=colnum(ref); maxc=max(maxc,ci)
        v=c.find(ns+'v'); isv=c.find(ns+'is')
        val=""
        if v is not None and v.text is not None: val=v.text
        elif isv is not None: val="".join(x.text or "" for x in isv.iter(ns+'t'))
        cells[ci]=val
    arr=[cells.get(i,"") for i in range(maxc+1)]
    rows.append(arr)
json.dump(rows,open("crm_rows.json","w"),ensure_ascii=False)
print("rows:",len(rows))
# print header + first rows
for i,r in enumerate(rows[:4]):
    print(i,"::"," | ".join(r))
