import zipfile,re
from xml.etree import ElementTree as ET
f="/root/.claude/uploads/7767e6b5-de9b-5631-a5c3-b77beef4874c/ae2485a5-Compiexe__Ind_pendance_Royale_S_nior_Habitat_1.xlsx"
z=zipfile.ZipFile(f)
print([n for n in z.namelist() if 'sheet' in n.lower() or 'shared' in n.lower()][:20])
ns='{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
# shared strings
ss=[]
if 'xl/sharedStrings.xml' in z.namelist():
    t=ET.fromstring(z.read('xl/sharedStrings.xml'))
    for si in t.findall(ns+'si'):
        ss.append("".join(x.text or "" for x in si.iter(ns+'t')))
print("sharedStrings:",len(ss))
# workbook sheet names
wb=ET.fromstring(z.read('xl/workbook.xml'))
for s in wb.findall(ns+'sheets/'+ns+'sheet'):
    print("SHEET:",s.get('name'), s.get('sheetId'))
