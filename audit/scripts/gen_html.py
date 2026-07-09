import json
m=json.load(open("master.json"))
anomalies=[
 {"sev":"CRITIQUE","titre":"Numéros F2026-16 à F2026-24 effacés du fichier de suivi",
  "preuve":"Fichier: lignes 47-55 de 'Suivi Factures' = montants sans numéro. Mail 10/06 (envoi à compta IRSH) + 15/06 (F23/F24). Les factures EXISTENT et ont été transmises.",
  "constat":"Le fichier de suivi a été vidé des numéros a posteriori alors que les factures sont bien émises et suivies par IRSH. Manipulation du suivi, pas perte de CA sur ces lignes."},
 {"sev":"CRITIQUE","titre":"Doublon de numéro F2026-17",
  "preuve":"Mail compta IRSH 10/06/2026: « j'ai deux factures avec le numéro F2026-17 ».",
  "constat":"Deux factures différentes ont porté le même numéro F2026-17 → risque comptable et de double comptabilisation."},
 {"sev":"ÉLEVÉE","titre":"Surfacturation vs montant DIA (F1225-02 PERRIERE)",
  "preuve":"Mail 23/04 camille.bustreau: F1225-02 PERRIERE MARIE CLAUDE DIAP133217 facturé 3250€ mais DIA=2065€.",
  "constat":"Facturation supérieure au barème DIA validé; facture révisée demandée. Vérifier d'autres écarts DIA↔facture."},
 {"sev":"ÉLEVÉE","titre":"PINCON SERGE — très actif, aucune facture retrouvée",
  "preuve":"Nombreux DIA/rework/visap (DIAP135285/135287, DIAR86325/86336, DIAV11424/11425). CRM: reworks/visap 'Posée/Effectuée'. Aucune facture dans onglets/suivi/mails. Pose au 'non facturé' ~1790€.",
  "constat":"Dossier réalisé et relancé (solde) mais jamais facturé côté suivi. À facturer/vérifier en priorité."},
 {"sev":"ÉLEVÉE","titre":"F2026-15 (DARMENDRAIL) — montant à corriger, non payée",
  "preuve":"Mails 18/06 & 09/07: F1225-01 annulée, 100€ déjà payés → F2026-15 doit être 100€ et non 200€. Toujours en attente au 09/07.",
  "constat":"Facture au mauvais montant, bloquée. À rééditer à 100€."},
 {"sev":"MOYENNE","titre":"Écart montant F2026-23 (fichier 4890 vs réel 4850)",
  "preuve":"Fichier 'Suivi Factures'=4890€; mail compta 09/07=4850€.",
  "constat":"Le fichier de suivi diverge de la facture réelle de 40€."},
 {"sev":"MOYENNE","titre":"Avoirs multiples SUPERCHI ARLETTE (AV07 + AV14)",
  "preuve":"Mails 21-22/05: 2 avoirs pour le même dossier (AV07=1020€ puis AV14=1967,25€), réclamations assurance successives.",
  "constat":"Double avoir sur un dossier sinistré; à rapprocher du contentieux assurance."},
 {"sev":"MOYENNE","titre":"Dossiers annulés après lancement (CORDINA FABRICE)",
  "preuve":"Mails 10/06 & 02/07 stephanie.bustreau: VERSAILLES ROSANNE _WS3501021 et DUBOUE GILLES _WS3515128 annulés.",
  "constat":"Commandes annulées 'de CORDINA FABRICE'; vérifier récupération matériel et absence de facturation."},
 {"sev":"INFO","titre":"Périmètre réel plus large que les 2 fichiers",
  "preuve":"Mails: réseaux ASH Europe (asheurope.com, projets PROJ…, HAMARIS/ERILIA/Haute-Savoie Habitat), Halpades (bons de commande), Ecoshower (Barros), SEM4V / LT Showertec (AO France Loire).",
  "constat":"La facturation 2026 dépasse IRSH+BARROS. Ces réseaux devront être audités (autre boîte mail pour Barros)."},
]
m["anomalies"]=anomalies
DATA=json.dumps(m,ensure_ascii=False)

html = '''<div id="app"></div>
<style>
:root{--bg:#eef1f5;--card:#fff;--tx:#12181f;--mut:#5b6675;--bd:#d5dbe3;--ac:#1f4e78;
 --red:#c0392b;--org:#c47a10;--grn:#1e8449;--blu:#2471a3;
 --red-bg:#fdecea;--red-tx:#a5281b;--org-bg:#fbf1d8;--org-tx:#8a5a06;--grn-bg:#e5f4ea;--grn-tx:#166534;--blu-bg:#e4eff8;--blu-tx:#1c5a86}
@media(prefers-color-scheme:dark){:root{--bg:#0e1319;--card:#19212c;--tx:#eef2f7;--mut:#a4b0be;--bd:#303a47;--ac:#5aa2e6;
 --red:#e8776b;--org:#e6b34d;--grn:#65c98d;--blu:#7fb3e0;
 --red-bg:#3d201c;--red-tx:#f3a89e;--org-bg:#3a2f14;--org-tx:#f0cd7e;--grn-bg:#173224;--grn-tx:#8fd9ad;--blu-bg:#152a3d;--blu-tx:#9cc7ec}}
:root[data-theme=dark]{--bg:#0e1319;--card:#19212c;--tx:#eef2f7;--mut:#a4b0be;--bd:#303a47;--ac:#5aa2e6;
 --red:#e8776b;--org:#e6b34d;--grn:#65c98d;--blu:#7fb3e0;
 --red-bg:#3d201c;--red-tx:#f3a89e;--org-bg:#3a2f14;--org-tx:#f0cd7e;--grn-bg:#173224;--grn-tx:#8fd9ad;--blu-bg:#152a3d;--blu-tx:#9cc7ec}
:root[data-theme=light]{--bg:#eef1f5;--card:#fff;--tx:#12181f;--mut:#5b6675;--bd:#d5dbe3;--ac:#1f4e78;
 --red:#c0392b;--org:#c47a10;--grn:#1e8449;--blu:#2471a3;
 --red-bg:#fdecea;--red-tx:#a5281b;--org-bg:#fbf1d8;--org-tx:#8a5a06;--grn-bg:#e5f4ea;--grn-tx:#166534;--blu-bg:#e4eff8;--blu-tx:#1c5a86}
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
table{border-collapse:collapse;width:100%;min-width:680px}
th,td{padding:8px 10px;text-align:left;border-bottom:1px solid var(--bd);font-size:13px;vertical-align:top}
th{position:sticky;top:0;background:var(--card);cursor:pointer;white-space:nowrap;color:var(--mut);font-size:12px;text-transform:uppercase;letter-spacing:.3px}
tbody tr:nth-child(even) td{background:rgba(127,127,127,.045)}
tbody tr:hover td{background:rgba(90,162,230,.14)}
td b{color:var(--ac);font-weight:700}
.wrap td:first-child b{font-size:13.5px}
.badge{padding:3px 9px;border-radius:20px;font-size:11px;font-weight:700;white-space:nowrap;border:1px solid transparent}
.b-oui{background:var(--red-bg);color:var(--red-tx);border-color:var(--red)}
.b-non{background:var(--grn-bg);color:var(--grn-tx);border-color:var(--grn)}
.b-verif{background:var(--org-bg);color:var(--org-tx);border-color:var(--org)}
.b-enc{background:var(--blu-bg);color:var(--blu-tx);border-color:var(--blu)}
.chip{display:inline-block;background:var(--blu-bg);color:var(--blu-tx);border:1px solid var(--bd);border-radius:5px;padding:1px 6px;margin:1px;font-size:11px;font-family:ui-monospace,monospace}
.det{background:var(--card);border:1px solid var(--bd);border-radius:10px;padding:16px;margin-bottom:12px}
.ev{border-left:3px solid var(--ac);padding:6px 10px;margin:8px 0;background:rgba(127,127,127,.05);border-radius:0 6px 6px 0}
.ev .m{color:var(--mut);font-size:12px}
.sev-CRITIQUE{border-left:5px solid var(--red)}.sev-ÉLEVÉE{border-left:5px solid var(--org)}.sev-MOYENNE{border-left:5px solid var(--blu)}.sev-INFO{border-left:5px solid var(--mut)}
.an{background:var(--card);border:1px solid var(--bd);border-radius:10px;padding:12px 14px;margin-bottom:10px}
.an h3{margin:4px 0 6px;font-size:15px}
.an .lab{display:inline-block;font-size:10px;font-weight:800;letter-spacing:.6px;padding:2px 8px;border-radius:12px}
.rc{background:var(--red-bg);color:var(--red-tx)}.ro{background:var(--org-bg);color:var(--org-tx)}.rb{background:var(--blu-bg);color:var(--blu-tx)}.rm{background:rgba(127,127,127,.15);color:var(--mut)}
button.x{padding:8px 12px;border:1px solid var(--ac);background:var(--ac);color:#fff;border-radius:8px;cursor:pointer;font-size:13px}
.small{font-size:12px;color:var(--mut)}
label.ck{display:flex;gap:6px;align-items:center;cursor:pointer}
</style>
<script>
const DATA=''' + DATA + ''';
const $=s=>document.querySelector(s);
let tab="dossiers", q="", fstat="", sortk="client", sortd=1;
const store=JSON.parse(localStorage.getItem("auditDecisions")||"{}");
function saveDec(k,v){store[k]=v;localStorage.setItem("auditDecisions",JSON.stringify(store));}
function badge(s){let c="b-verif";if(s.startsWith("Facturée"))c="b-non";else if(s.startsWith("Réalisée"))c="b-oui";else if(s.startsWith("Commande en cours"))c="b-enc";return `<span class="badge ${c}">${s}</span>`;}
function kpis(){const d=DATA.dossiers;const n=s=>d.filter(x=>x.status.startsWith(s)).length;
 return `<div class="kpis">
 <div class="kpi"><b>${d.length}</b><span>Dossiers IRSH</span></div>
 <div class="kpi"><b>${DATA.registre_factures.length}</b><span>Factures/avoirs au registre</span></div>
 <div class="kpi"><b style="color:var(--grn)">${n("Facturée")}</b><span>Facturées</span></div>
 <div class="kpi"><b style="color:var(--red)">${n("Réalisée")}</b><span>Réalisées NON facturées</span></div>
 <div class="kpi"><b style="color:var(--blu)">${d.filter(x=>x.status.startsWith("Commande en cours")).length}</b><span>Commandes en cours</span></div>
 <div class="kpi"><b style="color:var(--org)">${DATA.anomalies.length}</b><span>Anomalies</span></div>
 </div>`;}
function tabs(){const T=[["dossiers","Dossiers"],["afact","À facturer"],["reg","Registre factures"],["anom","Anomalies"],["evid","Preuves (mails)"]];
 return `<div class="tabs">`+T.map(([k,l])=>`<div class="tab ${tab==k?'on':''}" onclick="setTab('${k}')">${l}</div>`).join("")+`</div>`;}
window.setTab=k=>{tab=k;render();};
function statOpts(){const s=[...new Set(DATA.dossiers.map(d=>d.status))].sort();return `<option value="">— Tous statuts —</option>`+s.map(x=>`<option ${fstat==x?'selected':''}>${x}</option>`).join("");}
function rowsHtml(){let d=[...DATA.dossiers];
 if(q){const Q=q.toLowerCase();d=d.filter(x=>x.client.toLowerCase().includes(Q)||x.dia.join(" ").toLowerCase().includes(Q));}
 if(fstat)d=d.filter(x=>x.status==fstat);
 d.sort((a,b)=>{let A=(a[sortk]||"")+"",B=(b[sortk]||"")+"";return A<B?-1*sortd:A>B?sortd:0;});
 return `<div class="wrap"><table><thead><tr>
 <th onclick="sortBy('client')">Client</th><th>DIA</th><th onclick="sortBy('cp')">CP</th>
 <th onclick="sortBy('order_date')">Cmd (mail)</th><th onclick="sortBy('crm_status')">CRM</th>
 <th onclick="sortBy('invoice')">Facture</th><th onclick="sortBy('status')">Statut</th><th>Preuves</th><th>Ma décision</th></tr></thead><tbody>`+
 d.map((x,i)=>{const id=x.surname+"|"+x.client;const dec=store[id]||"";
  return `<tr onclick="openD('${encodeURIComponent(id)}')" style="cursor:pointer">
  <td><b>${x.client}</b></td><td>${x.dia.map(r=>`<span class=chip>${r}</span>`).join(" ")||"—"}</td>
  <td>${x.cp||""}</td><td class=small>${x.order_date||""}</td>
  <td class=small>${x.in_crm?(x.crm_type+" · "+x.crm_status):"—"}</td>
  <td>${x.invoice||"—"}</td><td>${badge(x.status)}</td>
  <td class=small>${x.evidence.length?("📎 "+x.evidence.length):""}</td>
  <td class=small>${dec?("✔ "+dec):""}</td></tr>`;}).join("")+`</tbody></table></div>
  <p class=small>${d.length} dossier(s) affiché(s). Cliquez une ligne pour voir les preuves et décider.</p>`;}
window.sortBy=k=>{if(sortk==k)sortd*=-1;else{sortk=k;sortd=1;}render();};
window.openD=eid=>{const id=decodeURIComponent(eid);const x=DATA.dossiers.find(d=>(d.surname+"|"+d.client)==id);if(!x)return;
 const dec=store[id]||"";
 let h=`<div class="det"><button class=x onclick="render()">← Retour</button>
 <h2 style="margin:10px 0 4px">${x.client} <span class=small>(${x.cp||"?"})</span></h2>
 <p>${badge(x.status)} &nbsp; DIA: ${x.dia.map(r=>`<span class=chip>${r}</span>`).join(" ")||"—"}</p>
 <table style="min-width:auto"><tbody>
 <tr><td class=small>Commande (1er mail)</td><td>${x.order_date||"—"}</td></tr>
 <tr><td class=small>CRM (07/07)</td><td>${x.in_crm?(x.crm_type+" — "+x.crm_status+" — "+x.crm_date):"absent du CRM"}</td></tr>
 <tr><td class=small>Pose (fichier)</td><td>${x.pose_date||"—"} ${x.montant?("· "+x.montant+"€"):""}</td></tr>
 <tr><td class=small>Facture</td><td>${x.invoice||"aucune retrouvée"}</td></tr>
 <tr><td class=small>Présent fichier / mail / CRM</td><td>${x.in_files?"fichier ":""}${x.in_mail?"mail ":""}${x.in_crm?"CRM":""}</td></tr>
 </tbody></table>
 <h3>Preuves retrouvées</h3>`;
 h+= x.evidence.length? x.evidence.map(e=>`<div class="ev"><div class="m">${e.date} · ${e.from} · <i>${e.subj}</i></div>${e.detail}</div>`).join("")
   : `<p class=small>Pas d'échange spécifique retrouvé (dossier connu par commande DIA et/ou fichier).</p>`;
 h+=`<h3>Votre décision</h3>
 <div class=ctl>${["À FACTURER","Déjà facturé","Non facturable (SAV/garantie)","À vérifier"].map(o=>`<label class=ck><input type=radio name=dec ${dec==o?'checked':''} onclick="setDec('${encodeURIComponent(id)}','${o}')"> ${o}</label>`).join("")}</div>
 </div>`;
 $("#app").innerHTML=`<h1>Détail dossier</h1>`+h;window.scrollTo(0,0);};
window.setDec=(eid,o)=>{saveDec(decodeURIComponent(eid),o);};
function afactHtml(){const d=DATA.dossiers.filter(x=>x.status.startsWith("Réalisée")||x.a_facturer=="OUI"||x.a_facturer=="À vérifier"&&x.in_crm);
 const done=DATA.dossiers.filter(x=>x.in_crm&&x.crm_status=="Posée/Effectuée"&&!x.invoice);
 return `<p class=small>Interventions <b>réalisées (CRM 07/07)</b> sans facture retrouvée = candidates à facturation. Statut de garantie à confirmer par vos soins.</p>
 <div class=wrap><table><thead><tr><th>Client</th><th>DIA</th><th>Type</th><th>Date</th><th>Statut</th><th>Décision</th></tr></thead><tbody>`+
 done.sort((a,b)=>a.crm_type<b.crm_type?-1:1).map(x=>{const id=x.surname+"|"+x.client;return `<tr onclick="openD('${encodeURIComponent(id)}')" style=cursor:pointer><td><b>${x.client}</b></td><td>${x.dia.map(r=>`<span class=chip>${r}</span>`).join(" ")}</td><td>${x.crm_type}</td><td class=small>${x.crm_date}</td><td>${badge(x.status)}</td><td class=small>${store[id]||""}</td></tr>`;}).join("")+`</tbody></table></div>`;}
function regHtml(){return `<div class=wrap><table><thead><tr><th>N° Facture</th><th>Date</th><th>Montant</th><th>État</th><th>Note / preuve</th></tr></thead><tbody>`+
 DATA.registre_factures.map(r=>`<tr><td><b>${r[0]}</b></td><td class=small>${r[1]}</td><td>${r[2]}</td><td>${r[3]}</td><td class=small>${r[4]}</td></tr>`).join("")+`</tbody></table></div>`;}
function anomHtml(){const col={CRITIQUE:"rc",ÉLEVÉE:"ro",MOYENNE:"rb",INFO:"rm"};
 return DATA.anomalies.map(a=>`<div class="an sev-${a.sev}"><div class="lab ${col[a.sev]}">${a.sev}</div><h3>${a.titre}</h3>
 <div class=small><b>Preuve:</b> ${a.preuve}</div><div style="margin-top:4px"><b>Constat:</b> ${a.constat}</div></div>`).join("");}
function evidHtml(){return DATA.evidence.map(e=>`<div class="ev"><div class="m">${e.date} · ${e.from} · <i>${e.subj}</i></div>${e.detail}</div>`).join("");}
window.exportDec=()=>{const rows=[["Client","DIA","Statut audit","Ma décision"]];
 DATA.dossiers.forEach(x=>{const id=x.surname+"|"+x.client;if(store[id])rows.push([x.client,x.dia.join(" "),x.status,store[id]]);});
 const csv=rows.map(r=>r.map(c=>'"'+(c+"").replace(/"/g,'""')+'"').join(";")).join("\\n");
 const b=new Blob([csv],{type:"text/csv"});const u=URL.createObjectURL(b);const a=document.createElement("a");a.href=u;a.download="mes_decisions_facturation.csv";a.click();};
function render(){let body="";
 if(tab=="dossiers")body=`<div class=ctl><input type=text placeholder="Rechercher client ou DIA…" value="${q}" oninput="q=this.value;render()"><select onchange="fstat=this.value;render()">${statOpts()}</select><button class=x onclick="exportDec()">⬇ Exporter mes décisions</button></div>`+rowsHtml();
 else if(tab=="afact")body=afactHtml();
 else if(tab=="reg")body=regHtml();
 else if(tab=="anom")body=anomHtml();
 else if(tab=="evid")body=`<p class=small>Événements de facturation retrouvés dans la boîte mail (source de vérité).</p>`+evidHtml();
 $("#app").innerHTML=`<h1>Audit Facturation 2026 — IRSH</h1><p class="sub">${DATA.perimetre} · généré ${DATA.generated} · données: fichier de suivi + boîte mail + CRM (07/07). Vos décisions sont enregistrées dans ce navigateur.</p>`+kpis()+tabs()+body;}
render();
</script>'''
open("Audit_IRSH_outil.html","w").write(html)
print("HTML écrit:",len(html),"octets")
