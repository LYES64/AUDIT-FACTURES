import base64
def uri(fn):
    b=base64.b64encode(open(fn,'rb').read()).decode()
    return "data:image/png;base64,"+b
LOGO=uri("logo.png"); PH=uri("douche_fade.png")
IT=uri("ic_tel.png"); IM=uri("ic_mail.png"); IP=uri("ic_pin.png"); IW=uri("ic_web.png")
people=[
 ("Loyk DUPORGE","Directeur général","07 83 64 96 64","+33783649664","loyk.duporge@adomsenior.fr","Loyk"),
 ("Lyes OUHADDAD","Gérant","06 79 79 59 93","+33679795993","lyes.ouhaddad@adomsenior.fr","Lyes"),
]
def sig(name,role,tel,telraw,mail):
    return f'''
<table cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;font-family:Arial,Helvetica,sans-serif;width:660px">
 <tr><td style="padding:0 0 12px 2px"><img src="{LOGO}" alt="Adomsenior" width="200" style="display:block;border:0"></td></tr>
 <tr><td style="padding:0">
   <table cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;width:100%"><tr>
     <td style="height:3px;background:#0F3B45;width:62%;font-size:0;line-height:0">&nbsp;</td>
     <td style="height:3px;background:#DB8A38;width:38%;font-size:0;line-height:0">&nbsp;</td>
   </tr></table>
 </td></tr>
 <tr><td style="padding:14px 0 0">
  <table cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;width:100%"><tr>
    <td style="vertical-align:middle;padding-right:8px">
      <div style="font-size:21px;font-weight:bold;color:#17242B">{name}</div>
      <div style="font-size:12px;font-weight:bold;letter-spacing:1px;color:#DB8A38;text-transform:uppercase;padding:3px 0 10px">{role} &middot; ADOMSENIOR</div>
      <table cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;font-size:13px;color:#33414a">
        <tr><td style="padding:3px 8px 3px 0"><img src="{IT}" width="14" height="14" style="display:block;border:0"></td><td style="padding:3px 0"><a href="tel:{telraw}" style="color:#33414a;text-decoration:none">{tel}</a></td></tr>
        <tr><td style="padding:3px 8px 3px 0"><img src="{IM}" width="14" height="14" style="display:block;border:0"></td><td style="padding:3px 0"><a href="mailto:{mail}" style="color:#0F3B45;text-decoration:none">{mail}</a></td></tr>
        <tr><td style="padding:3px 8px 3px 0"><img src="{IP}" width="14" height="14" style="display:block;border:0"></td><td style="padding:3px 0">2 impasse Joliot Curie, 64110 Juran&ccedil;on</td></tr>
        <tr><td style="padding:3px 8px 3px 0"><img src="{IW}" width="14" height="14" style="display:block;border:0"></td><td style="padding:3px 0"><a href="https://adomsenior.fr" style="color:#0F3B45;text-decoration:none">adomsenior.fr</a></td></tr>
      </table>
    </td>
    <td style="vertical-align:middle;width:210px;text-align:right"><img src="{PH}" alt="Douche s&eacute;curis&eacute;e Adomsenior" width="205" style="display:block;border:0;margin-left:auto"></td>
  </tr></table>
 </td></tr>
 <tr><td style="padding:10px 0 0;font-size:10.5px;color:#8a99a0;line-height:1.5">
   <b style="color:#0F3B45">Bien chez soi</b> &mdash; Am&eacute;nagement &amp; adaptation du logement des seniors &middot; Douches s&eacute;curis&eacute;es.<br>
   SIRET 849&nbsp;109&nbsp;558&nbsp;00023 &middot; Ce message et ses pi&egrave;ces jointes sont confidentiels.
 </td></tr>
</table>'''

# standalone (for PNG preview)
for name,role,tel,telraw,mail,short in people:
    html=f'<!doctype html><meta charset="utf-8"><body style="margin:0;background:#fff"><div id="sig" style="display:inline-block;padding:22px;background:#fff">{sig(name,role,tel,telraw,mail)}</div></body>'
    open(f"sig2_{short}.html","w").write(html)

# combined deliverable
blocks=""
for name,role,tel,telraw,mail,short in people:
    blocks+=f'<p style="font-size:13px;color:#888;margin:22px 0 8px;font-family:Arial"><b>Signature — {name} ({role})</b></p><div style="border:1px solid #e2e6ec;border-radius:8px;padding:18px;background:#fff">{sig(name,role,tel,telraw,mail)}</div>'
deliver=f'''<!doctype html><meta charset="utf-8">
<div style="font-family:Arial,Helvetica,sans-serif;max-width:820px;margin:0 auto;padding:20px;color:#1b2230">
<h2>Signatures cliquables — ADOMSENIOR</h2>
<p style="font-size:14px;color:#555;line-height:1.6">Signatures <b>HTML avec liens cliquables</b> (t&eacute;l&eacute;phone, e-mail, site). Photo &agrave; bords fondus (transparence).</p>
<p style="font-size:13px;color:#166534;background:#e5f4ea;border:1px solid #a7d8ba;border-radius:6px;padding:10px 12px;line-height:1.55">
<b>Installer dans Gmail :</b> ouvrez ce fichier dans un navigateur &rarr; s&eacute;lectionnez une signature (glisser la souris dessus) &rarr; <b>Ctrl/Cmd+C</b> &rarr; Gmail &rarr; Param&egrave;tres &rarr; Signature &rarr; <b>Ctrl/Cmd+V</b>. Gmail h&eacute;berge automatiquement les images au collage et garde les liens cliquables.</p>
{blocks}
</div>'''
open("signatures_ADOMSENIOR_cliquables.html","w").write(deliver)
print("built html; deliverable size KB:", len(deliver)//1024)
