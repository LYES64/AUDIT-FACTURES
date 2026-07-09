import json
m=json.load(open("master2.json"))
DATA=json.dumps(m,ensure_ascii=False)
CSS='''
:root{--bg:#eef1f5;--card:#fff;--tx:#12181f;--mut:#5b6675;--bd:#d5dbe3;--ac:#1f4e78;
 --red:#c0392b;--org:#c47a10;--grn:#1e8449;--blu:#2471a3;
 --red-bg:#fdecea;--red-tx:#a5281b;--org-bg:#fbf1d8;--org-tx:#8a5a06;--grn-bg:#e5f4ea;--grn-tx:#166534;--blu-bg:#e4eff8;--blu-tx:#1c5a86}
@media(prefers-color-scheme:dark){:root{--bg:#0e1319;--card:#19212c;--tx:#eef2f7;--mut:#a4b0be;--bd:#303a47;--ac:#5aa2e6;
 --red:#e8776b;--org:#e6b34d;--grn:#65c98d;--blu:#7fb3e0;
 --red-bg:#3d201c;--red-tx:#f3a89e;--org-bg:#3a2f14;--org-tx:#f0cd7e;--grn-bg:#173224;--grn-tx:#8fd9ad;--blu-bg:#152a3d;--blu-tx:#9cc7ec}}
:root[data-theme=dark]{--bg:#0e1319;--card:#19212c;--tx:#eef2f7;--mut:#a4b0be;--bd:#303a47;--ac:#5aa2e6;--red:#e8776b;--org:#e6b34d;--grn:#65c98d;--blu:#7fb3e0;--red-bg:#3d201c;--red-tx:#f3a89e;--org-bg:#3a2f14;--org-tx:#f0cd7e;--grn-bg:#173224;--grn-tx:#8fd9ad;--blu-bg:#152a3d;--blu-tx:#9cc7ec}
:root[data-theme=light]{--bg:#eef1f5;--card:#fff;--tx:#12181f;--mut:#5b6675;--bd:#d5dbe3;--ac:#1f4e78;--red:#c0392b;--org:#c47a10;--grn:#1e8449;--blu:#2471a3;--red-bg:#fdecea;--red-tx:#a5281b;--org-bg:#fbf1d8;--org-tx:#8a5a06;--grn-bg:#e5f4ea;--grn-tx:#166534;--blu-bg:#e4eff8;--blu-tx:#1c5a86}
*{box-sizing:border-box}body{margin:0}
#app{font-family:-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;color:var(--tx);background:var(--bg);min-height:100vh;padding:16px;font-size:14px}
h1{font-size:20px;margin:0 0 2px}.sub{color:var(--mut);margin:0 0 14px;font-size:13px}
.kpis{display:flex;flex-wrap:wrap;gap:10px;margin-bottom:14px}
.kpi{background:var(--card);border:1px solid var(--bd);border-radius:10px;padding:10px 14px;min-width:120px}
.kpi b{font-size:22px;display:block}.kpi span{color:var(--mut);font-size:12px}
.tabs{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:12px}
.tab{padding:7px 13px;border:1px solid var(--bd);background:var(--card);border-radius:8px;cursor:pointer;font-size:13px}
.tab.on{background:var(--ac);color:#fff;border-color:var(--ac)}
.ctl{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:10px}
input,select{padding:8px 10px;border:1px solid var(--bd);border-radius:8px;background:var(--card);color:var(--tx);font-size:13px}
input[type=text]{min-width:220px;flex:1}
.wrap{overflow-x:auto;background:var(--card);border:1px solid var(--bd);border-radius:10px}
table{border-collapse:collapse;width:100%;min-width:640px}
th,td{padding:8px 10px;text-align:left;border-bottom:1px solid var(--bd);font-size:13px;vertical-align:top}
th{position:sticky;top:0;background:var(--card);color:var(--mut);font-size:12px;text-transform:uppercase;letter-spacing:.3px;white-space:nowrap}
tbody tr:nth-child(even) td{background:rgba(127,127,127,.045)}
tbody tr:hover td{background:rgba(90,162,230,.14)}
td b{color:var(--ac);font-weight:700}
.badge{padding:3px 9px;border-radius:20px;font-size:11px;font-weight:700;white-space:nowrap;border:1px solid transparent;display:inline-block}
.p-Payée{background:var(--grn-bg);color:var(--grn-tx);border-color:var(--grn)}
.p-Non{background:var(--red-bg);color:var(--red-tx);border-color:var(--red)}
.p-Partielle,.p-À{background:var(--org-bg);color:var(--org-tx);border-color:var(--org)}
.p-Avoir{background:var(--blu-bg);color:var(--blu-tx);border-color:var(--blu)}
.b-non{background:var(--grn-bg);color:var(--grn-tx);border:1px solid var(--grn)}
.b-oui{background:var(--red-bg);color:var(--red-tx);border:1px solid var(--red)}
.b-verif{background:var(--org-bg);color:var(--org-tx);border:1px solid var(--org)}
.b-enc{background:var(--blu-bg);color:var(--blu-tx);border:1px solid var(--blu)}
.chip{display:inline-block;background:var(--blu-bg);color:var(--blu-tx);border:1px solid var(--bd);border-radius:5px;padding:1px 6px;margin:1px;font-size:11px;font-family:ui-monospace,monospace}
.card{background:var(--card);border:1px solid var(--bd);border-radius:10px;padding:14px 16px;margin-bottom:12px}
.reprise{border-left:5px solid var(--ac)}
.reprise h3{margin:0 0 6px}.big{font-size:18px;font-weight:800;color:var(--ac)}
.an{background:var(--card);border:1px solid var(--bd);border-radius:10px;padding:12px 14px;margin-bottom:10px}
.sev-CRITIQUE{border-left:5px solid var(--red)}.sev-ÉLEVÉE{border-left:5px solid var(--org)}.sev-MOYENNE{border-left:5px solid var(--blu)}.sev-INFO{border-left:5px solid var(--mut)}
.an h3{margin:4px 0 6px;font-size:15px}
.lab{display:inline-block;font-size:10px;font-weight:800;letter-spacing:.6px;padding:2px 8px;border-radius:12px}
.rc{background:var(--red-bg);color:var(--red-tx)}.ro{background:var(--org-bg);color:var(--org-tx)}.rb{background:var(--blu-bg);color:var(--blu-tx)}.rm{background:rgba(127,127,127,.15);color:var(--mut)}
.ev{border-left:3px solid var(--ac);padding:6px 10px;margin:8px 0;background:rgba(127,127,127,.05);border-radius:0 6px 6px 0}
.ev .m{color:var(--mut);font-size:12px}
.small{font-size:12px;color:var(--mut)}
.pill{display:inline-block;padding:2px 8px;border-radius:12px;font-size:11px;font-weight:700;background:var(--ac);color:#fff}
'''
JS='''
const DATA=__DATA__;
const $=s=>document.querySelector(s);
let tab="synth",q="",fp="";
function pbadge(s){const k=s.split(" ")[0];return `<span class="badge p-${k}">${s}</span>`;}
function regTable(reg,who){
 let rows=reg;
 if(fp) rows=rows.filter(r=>r[3].startsWith(fp));
 return `<div class=wrap><table><thead><tr><th>N° Facture</th><th>Date</th><th>Montant €</th><th>Paiement</th><th>Source / détail</th></tr></thead><tbody>`+
 rows.map(r=>`<tr><td><b>${r[0]}</b></td><td class=small>${r[1]}</td><td>${r[2]}</td><td>${pbadge(r[3])}</td><td class=small>${r[4]}</td></tr>`).join("")+
 `</tbody></table></div><p class=small>${rows.length} lignes. * = date antidatée (voir anomalies).</p>`;}
function payCount(reg,pre){return reg.filter(r=>r[3].startsWith(pre)).length;}
function reprBlock(k){const r=DATA.reprise[k];return `<div class="card reprise"><h3>${k}</h3>
 <div class=small>Dernière facture émise :</div><div style="margin:2px 0 8px">${r.derniere}</div>
 <div class=small>➡️ Reprendre la numérotation à :</div><div class=big>${r.repartir}</div>
 <div class=small style="margin-top:6px">Avoirs : ${r.avoir}</div>
 <div class=small style="margin-top:6px;color:var(--org-tx)">${r.note}</div></div>`;}
function synth(){
 const ri=DATA.reg_irsh, rb=DATA.reg_barros;
 return `<div class=kpis>
  <div class=kpi><b>${ri.length+rb.length}</b><span>Factures/avoirs recensés</span></div>
  <div class=kpi><b style="color:var(--grn)">${payCount(ri,'Payée')+payCount(rb,'Payée')}</b><span>Payées</span></div>
  <div class=kpi><b style="color:var(--red)">${payCount(ri,'Non')+payCount(rb,'Non')}</b><span>Non payées</span></div>
  <div class=kpi><b style="color:var(--org)">${DATA.anomalies.length}</b><span>Anomalies</span></div>
  <div class=kpi><b>${DATA.dossiers.length}</b><span>Dossiers IRSH</span></div></div>
 <h2 style="font-size:16px;margin:6px 0">Reprise de la numérotation</h2>
 <div style="display:flex;gap:12px;flex-wrap:wrap">${reprBlock('IRSH')}${reprBlock('BARROS')}</div>
 <div class=card><b>Comment lire l'état de paiement</b><div class=small style="margin-top:6px">
 Source IRSH : colonnes « État/Date règlement » du fichier + mails de la compta IRSH (Camille Bustreau), le plus récent = 09/07/2026.<br>
 Source BARROS : fichier + détail des virements de Marina Delage (Eco Shower) du 19/05, + notifications bancaires Qonto.<br>
 <span class="badge p-Payée">Payée</span> confirmée · <span class="badge p-Non">Non payée</span> due · <span class="badge p-À">À vérifier</span> · <span class="badge p-Avoir">Avoir</span></div></div>`;}
function anom(){return DATA.anomalies.map(a=>{const c={CRITIQUE:'rc',ÉLEVÉE:'ro',MOYENNE:'rb',INFO:'rm'}[a.sev];
 return `<div class="an sev-${a.sev}"><span class="lab ${c}">${a.sev}</span><h3>${a.titre}</h3>
 <div class=small><b>Preuve :</b> ${a.preuve}</div><div style="margin-top:4px"><b>Constat :</b> ${a.constat}</div></div>`;}).join("");}
function doss(){let d=[...DATA.dossiers];const Q=q.toLowerCase();
 if(q)d=d.filter(x=>x.client.toLowerCase().includes(Q)||x.dia.join(" ").toLowerCase().includes(Q));
 return `<div class=ctl><input type=text placeholder="Rechercher client / DIA…" value="${q}" oninput="q=this.value;render()"></div>
 <div class=wrap><table><thead><tr><th>Client</th><th>DIA</th><th>CRM</th><th>Facture</th><th>Statut</th><th>Preuves</th></tr></thead><tbody>`+
 d.map(x=>`<tr><td><b>${x.client}</b></td><td>${x.dia.map(r=>`<span class=chip>${r}</span>`).join(" ")||"—"}</td>
 <td class=small>${x.in_crm?(x.crm_type+" · "+x.crm_status):"—"}</td><td>${x.invoice||"—"}</td>
 <td class=small>${x.status}</td><td class=small>${x.evidence.length?("📎"+x.evidence.length):""}</td></tr>`).join("")+
 `</tbody></table></div><p class=small>${d.length} dossiers IRSH.</p>`;}
function evid(){return DATA.evidence.map(e=>`<div class=ev><div class=m>${e.date} · ${e.from} · <i>${e.subj}</i></div>${e.detail}</div>`).join("");}
const T=[["synth","Synthèse & Reprise"],["fi","Factures IRSH"],["fb","Factures BARROS"],["do","Dossiers IRSH"],["an","Anomalies"],["ev","Preuves (mails)"]];
window.setTab=k=>{tab=k;fp="";render();};
window.setFp=v=>{fp=v;render();};
function payFilter(){return `<div class=ctl><select onchange="setFp(this.value)">
 <option value="">— Tout paiement —</option><option value="Payée" ${fp=='Payée'?'selected':''}>Payées</option>
 <option value="Non" ${fp=='Non'?'selected':''}>Non payées</option><option value="À" ${fp=='À'?'selected':''}>À vérifier</option>
 <option value="Avoir" ${fp=='Avoir'?'selected':''}>Avoirs</option></select></div>`;}
function render(){let b="";
 if(tab=="synth")b=synth();
 else if(tab=="fi")b=`<h2 style="font-size:16px">Factures IRSH → Indépendance Royale</h2>`+payFilter()+regTable(DATA.reg_irsh,'IRSH');
 else if(tab=="fb")b=`<h2 style="font-size:16px">Factures BARROS / Eco Shower</h2>`+payFilter()+regTable(DATA.reg_barros,'BARROS');
 else if(tab=="do")b=doss();
 else if(tab=="an")b=anom();
 else if(tab=="ev")b=`<p class=small>Événements de facturation retrouvés dans les boîtes mail (source de vérité).</p>`+evid();
 $("#app").innerHTML=`<h1>Audit Facturation 2026 — ETS OUHADDAD</h1>
 <p class=sub>IRSH (Indépendance Royale) + BARROS (Eco Shower) · généré ${DATA.generated} · sources: fichiers de suivi + boîtes mail + CRM IRSH</p>
 <div class=tabs>${T.map(([k,l])=>`<div class="tab ${tab==k?'on':''}" onclick="setTab('${k}')">${l}</div>`).join("")}</div>`+b;}
render();
'''
html='<div id="app"></div>\n<style>'+CSS+'</style>\n<script>'+JS.replace("__DATA__",DATA)+'</script>'
open("Audit_Factures_outil.html","w").write(html)
print("HTML v2 écrit:",len(html))
