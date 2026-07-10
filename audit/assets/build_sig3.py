BASE="https://adomsenior.fr/signature/"   # <-- à remplacer par votre URL d'hébergement
people=[
 ("Loyk DUPORGE","Directeur général","07 83 64 96 64","+33783649664","loyk.duporge@adomsenior.fr"),
 ("Lyes OUHADDAD","Gérant","06 79 79 59 93","+33679795993","lyes.ouhaddad@adomsenior.fr"),
]
def row(lbl,inner):
    return f'<tr><td style="padding:2px 10px 2px 0;font-size:12px;font-weight:bold;color:#0F3B45">{lbl}</td><td style="padding:2px 0;font-size:13px;color:#33414a">{inner}</td></tr>'
def sig(name,role,tel,telraw,mail):
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
       {row("T&eacute;l",f'<a href="tel:{telraw}" style="color:#33414a;text-decoration:none">{tel}</a>')}
       {row("Mail",f'<a href="mailto:{mail}" style="color:#0F3B45;text-decoration:none">{mail}</a>')}
       {row("Adr","2 impasse Joliot Curie, 64110 Juran&ccedil;on")}
       {row("Web",'<a href="https://adomsenior.fr" style="color:#0F3B45;text-decoration:none">adomsenior.fr</a>')}
     </table>
   </td>
   <td style="vertical-align:middle;width:210px;text-align:right"><img src="{BASE}douche_fade.png" alt="Douche s&eacute;curis&eacute;e" width="205" style="display:block;border:0;margin-left:auto"></td>
 </tr></table></td></tr>
 <tr><td style="padding:10px 0 0;font-size:10.5px;color:#8a99a0;line-height:1.5">
   <b style="color:#0F3B45">Bien chez soi</b> &mdash; Am&eacute;nagement &amp; adaptation du logement des seniors &middot; Douches s&eacute;curis&eacute;es.<br>
   SIRET 849&nbsp;109&nbsp;558&nbsp;00023 &middot; Ce message et ses pi&egrave;ces jointes sont confidentiels.</td></tr>
</table>'''
blocks=""
for name,role,tel,telraw,mail in people:
    blocks+=f'<p style="font-size:13px;color:#888;margin:22px 0 8px;font-family:Arial"><b>Signature — {name} ({role})</b></p><div style="border:1px solid #e2e6ec;border-radius:8px;padding:18px;background:#fff">{sig(name,role,tel,telraw,mail)}</div>'
deliver=f'''<!doctype html><meta charset="utf-8">
<div style="font-family:Arial,Helvetica,sans-serif;max-width:820px;margin:0 auto;padding:20px;color:#1b2230">
<h2>Signatures cliquables (l&eacute;g&egrave;res) — ADOMSENIOR</h2>
<p style="font-size:13px;color:#b9770e;background:#fff4e0;border:1px solid #f0d090;border-radius:6px;padding:10px 12px;line-height:1.55">
<b>Avant d'utiliser :</b> h&eacute;bergez <b>logo.png</b> et <b>douche_fade.png</b> sur votre site, puis remplacez partout l'URL
<code>{BASE}</code> par votre URL r&eacute;elle (ex. <code>https://adomsenior.fr/signature/</code>). Sans &ccedil;a les images ne s'afficheront pas.</p>
<p style="font-size:13px;color:#166534;background:#e5f4ea;border:1px solid #a7d8ba;border-radius:6px;padding:10px 12px;line-height:1.55">
<b>Gmail :</b> ouvrez ce fichier dans un navigateur (une fois les images en ligne) &rarr; s&eacute;lectionnez une signature &rarr; Ctrl/Cmd+C &rarr; Gmail &rarr; Param&egrave;tres &rarr; Signature &rarr; Ctrl/Cmd+V. La signature est l&eacute;g&egrave;re : <b>taille accept&eacute;e</b>.</p>
{blocks}</div>'''
open("signatures_ADOMSENIOR_hebergee.html","w").write(deliver)
print("size KB:", len(deliver)//1024)
