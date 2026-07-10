BASE="https://raw.githubusercontent.com/LYES64/AUDIT-FACTURES/4f4f872f100d260d3b93a225a15b764ebe863331/audit/assets/"
people=[
 ("Loyk DUPORGE","Directeur général","07 83 64 96 64","+33783649664","loyk.duporge@adomsenior.fr","Loyk"),
 ("Lyes OUHADDAD","Gérant","06 79 79 59 93","+33679795993","lyes.ouhaddad@adomsenior.fr","Lyes"),
]
def sig(name,role,tel,telraw,mail):
    I=lambda n:f'<img src="{BASE}{n}" width="14" height="14" style="display:block;border:0">'
    r=lambda ic,inner:f'<tr><td style="padding:3px 8px 3px 0">{ic}</td><td style="padding:3px 0;font-size:13px;color:#33414a">{inner}</td></tr>'
    return f'''<table cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;font-family:Arial,Helvetica,sans-serif;width:640px">
 <tr><td style="padding:0 0 12px 2px"><img src="{BASE}logo.png" alt="Adomsenior" width="200" style="display:block;border:0"></td></tr>
 <tr><td><table cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;width:100%"><tr>
   <td style="height:3px;background:#0F3B45;width:62%;font-size:0;line-height:0">&nbsp;</td>
   <td style="height:3px;background:#DB8A38;width:38%;font-size:0;line-height:0">&nbsp;</td></tr></table></td></tr>
 <tr><td style="padding:14px 0 0"><table cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;width:100%"><tr>
   <td style="vertical-align:middle">
     <div style="font-size:21px;font-weight:bold;color:#17242B">{name}</div>
     <div style="font-size:12px;font-weight:bold;letter-spacing:1px;color:#DB8A38;text-transform:uppercase;padding:3px 0 10px">{role} &middot; ADOMSENIOR</div>
     <table cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse">
       {r(I("ic_tel.png"),f'<a href="tel:{telraw}" style="color:#33414a;text-decoration:none">{tel}</a>')}
       {r(I("ic_mail.png"),f'<a href="mailto:{mail}" style="color:#0F3B45;text-decoration:none">{mail}</a>')}
       {r(I("ic_pin.png"),"2 impasse Joliot Curie, 64110 Juran&ccedil;on")}
       {r(I("ic_web.png"),'<a href="https://adomsenior.fr" style="color:#0F3B45;text-decoration:none">adomsenior.fr</a>')}
     </table></td>
   <td style="vertical-align:middle;width:236px;text-align:right"><img src="{BASE}douche_diag.png" alt="Douche s&eacute;curis&eacute;e Adomsenior" width="232" style="display:block;border:0;margin-left:auto"></td>
 </tr></table></td></tr>
 <tr><td style="padding:10px 0 0;font-size:10.5px;color:#8a99a0;line-height:1.5">
   <b style="color:#0F3B45">Bien chez soi</b> &mdash; Am&eacute;nagement &amp; adaptation du logement des seniors &middot; Douches s&eacute;curis&eacute;es.<br>
   SIRET 849&nbsp;109&nbsp;558&nbsp;00023 &middot; Ce message et ses pi&egrave;ces jointes sont confidentiels.</td></tr>
</table>'''
# standalone previews
for name,role,tel,telraw,mail,short in people:
    open(f"sig5_{short}.html","w").write(f'<!doctype html><meta charset=utf-8><body style="margin:0;background:#fff"><div id="sig" style="display:inline-block;padding:22px;background:#fff">{sig(name,role,tel,telraw,mail)}</div></body>')
# deliverable
blocks="".join(f'<p style="font-size:13px;color:#888;margin:22px 0 8px;font-family:Arial"><b>Signature — {n} ({rl})</b></p><div style="border:1px solid #e2e6ec;border-radius:8px;padding:18px;background:#fff">{sig(n,rl,t,tr,m)}</div>' for n,rl,t,tr,m,s in people)
deliver=f'''<!doctype html><meta charset="utf-8">
<div style="font-family:Arial,Helvetica,sans-serif;max-width:820px;margin:0 auto;padding:20px;color:#1b2230">
<h2>Signatures ADOMSENIOR — cliquables (photo en d&eacute;coupe diagonale)</h2>
<p style="font-size:13px;color:#166534;background:#e5f4ea;border:1px solid #a7d8ba;border-radius:6px;padding:10px 12px;line-height:1.55">
<b>Gmail :</b> ouvrez ce fichier dans un navigateur &rarr; s&eacute;lectionnez une signature &agrave; la souris &rarr; Ctrl/Cmd+C &rarr; Gmail &rarr; Param&egrave;tres &rarr; Signature &rarr; Ctrl/Cmd+V. Images h&eacute;berg&eacute;es (liens) &rarr; <b>taille l&eacute;g&egrave;re, accept&eacute;e</b>. Liens t&eacute;l/mail/site cliquables.</p>
{blocks}</div>'''
open("signatures_ADOMSENIOR_final.html","w").write(deliver)
print("deliver KB:", len(deliver)//1024)
