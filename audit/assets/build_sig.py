logo=open("logo.svg").read()
bath=open("bathroom.svg").read()
people=[
 ("Loyk DUPORGE","Directeur général","07 83 64 96 64","loyk.duporge@adomsenior.fr","sig_Loyk_Duporge"),
 ("Lyes OUHADDAD","Gérant","06 79 79 59 93","lyes.ouhaddad@adomsenior.fr","sig_Lyes_Ouhaddad"),
]
ICON={
 "tel":'<svg width="15" height="15" viewBox="0 0 24 24" fill="#0F3B45"><path d="M6.6 10.8c1.4 2.8 3.8 5.2 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1C10.6 21 3 13.4 3 4c0-.6.4-1 1-1h3.4c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.4 0 .8-.3 1z"/></svg>',
 "mail":'<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#0F3B45" stroke-width="2"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M4 7l8 6 8-6"/></svg>',
 "pin":'<svg width="15" height="15" viewBox="0 0 24 24" fill="#0F3B45"><path d="M12 2a7 7 0 0 0-7 7c0 5 7 13 7 13s7-8 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 12 6a2.5 2.5 0 0 1 0 5.5z"/></svg>',
 "web":'<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#0F3B45" stroke-width="1.8"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/></svg>',
}
TPL='''<!doctype html><meta charset="utf-8">
<style>
 *{{margin:0;padding:0;box-sizing:border-box}}
 body{{background:#fff}}
 #sig{{width:720px;background:#ffffff;padding:24px 26px;font-family:Arial,Helvetica,sans-serif}}
 .logo svg{{height:52px;width:auto;display:block}}
 .rule{{height:3px;background:linear-gradient(90deg,#0F3B45 0%,#0F3B45 62%,#DB8A38 62%,#DB8A38 100%);border-radius:2px;margin:14px 0 16px}}
 .row{{display:flex;align-items:center;gap:22px}}
 .info{{flex:1}}
 .name{{font-size:21px;font-weight:800;color:#17242B;letter-spacing:.2px}}
 .role{{font-size:12px;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:#DB8A38;margin:3px 0 10px}}
 .line{{font-size:13px;color:#33414a;line-height:1.95;display:flex;align-items:center;gap:9px}}
 .line svg{{flex:none}}
 a{{color:#0F3B45;text-decoration:none}}
 .bath{{width:196px;flex:none}}
 .bath svg{{width:196px;height:auto;display:block;border-radius:14px;box-shadow:0 6px 18px rgba(15,59,69,.16)}}
 .foot{{font-size:10.5px;color:#8a99a0;margin-top:14px;line-height:1.5}}
 .foot b{{color:#0F3B45}}
</style>
<div id="sig">
  <div class="logo">{logo}</div>
  <div class="rule"></div>
  <div class="row">
    <div class="info">
      <div class="name">{name}</div>
      <div class="role">{role} &middot; ADOMSENIOR</div>
      <div class="line">{ic_tel} <span>{tel}</span></div>
      <div class="line">{ic_mail} <a href="mailto:{mail}">{mail}</a></div>
      <div class="line">{ic_pin} <span>2 impasse Joliot Curie, 64110 Juran&ccedil;on</span></div>
      <div class="line">{ic_web} <a href="https://adomsenior.fr">adomsenior.fr</a></div>
    </div>
    <div class="bath">{bath}</div>
  </div>
  <div class="foot"><b>Bien chez soi</b> &mdash; Am&eacute;nagement &amp; adaptation du logement des seniors &middot; Douches s&eacute;curis&eacute;es.<br>
  SIRET 849&nbsp;109&nbsp;558&nbsp;00023 &middot; Ce message et ses pi&egrave;ces jointes sont confidentiels.</div>
</div>'''
for name,role,tel,mail,fn in people:
    html=TPL.format(logo=logo,bath=bath,name=name,role=role,tel=tel,mail=mail,
                    ic_tel=ICON["tel"],ic_mail=ICON["mail"],ic_pin=ICON["pin"],ic_web=ICON["web"])
    open(fn+".html","w").write(html)
print("built")
