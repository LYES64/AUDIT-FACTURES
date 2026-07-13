#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
m = json.load(open("audit/data/master4.json", encoding="utf-8"))
DATA = json.dumps(m, ensure_ascii=False)

CSS = r'''
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
.kpi{background:var(--card);border:1px solid var(--bd);border-radius:10px;padding:10px 14px;min-width:120px;cursor:default}
.kpi.clk{cursor:pointer}.kpi.clk:hover{border-color:var(--ac)}
.kpi.on{border-color:var(--ac);box-shadow:0 0 0 2px var(--ac) inset}
.kpi b{font-size:22px;display:block}.kpi span{color:var(--mut);font-size:12px}
.tabs{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:12px}
.tab{padding:7px 13px;border:1px solid var(--bd);background:var(--card);border-radius:8px;cursor:pointer;font-size:13px}
.tab.on{background:var(--ac);color:#fff;border-color:var(--ac)}
.tab.alert{border-color:var(--red)}.tab.alert.on{background:var(--red);border-color:var(--red)}
.ctl{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:10px;align-items:center}
input,select{padding:8px 10px;border:1px solid var(--bd);border-radius:8px;background:var(--card);color:var(--tx);font-size:13px}
input[type=text]{min-width:220px;flex:1}
.wrap{overflow-x:auto;background:var(--card);border:1px solid var(--bd);border-radius:10px}
table{border-collapse:collapse;width:100%;min-width:640px}
th,td{padding:8px 10px;text-align:left;border-bottom:1px solid var(--bd);font-size:13px;vertical-align:top}
th{position:sticky;top:0;background:var(--card);color:var(--mut);font-size:12px;text-transform:uppercase;letter-spacing:.3px;white-space:nowrap}
th.sortable{cursor:pointer;user-select:none}th.sortable:hover{color:var(--ac)}
th .ar{opacity:.5;font-size:10px}
tbody tr:nth-child(even) td{background:rgba(127,127,127,.045)}
tbody tr:hover td{background:rgba(90,162,230,.14)}
td b{color:var(--ac);font-weight:700}
.badge{padding:3px 9px;border-radius:20px;font-size:11px;font-weight:700;white-space:nowrap;border:1px solid transparent;display:inline-block}
.p-Payée{background:var(--grn-bg);color:var(--grn-tx);border-color:var(--grn)}
.p-Non{background:var(--red-bg);color:var(--red-tx);border-color:var(--red)}
.p-Partielle,.p-À{background:var(--org-bg);color:var(--org-tx);border-color:var(--org)}
.p-Avoir{background:var(--blu-bg);color:var(--blu-tx);border-color:var(--blu)}
.f-fac{background:var(--grn-bg);color:var(--grn-tx);border:1px solid var(--grn)}
.f-non{background:var(--red-bg);color:var(--red-tx);border:1px solid var(--red)}
.f-enc{background:var(--blu-bg);color:var(--blu-tx);border:1px solid var(--blu)}
.f-ver{background:var(--org-bg);color:var(--org-tx);border:1px solid var(--org)}
.f-off{background:rgba(127,127,127,.15);color:var(--mut);border:1px solid var(--mut)}
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
.note{background:var(--org-bg);color:var(--org-tx);border:1px solid var(--org);border-radius:8px;padding:10px 12px;font-size:13px;margin-bottom:12px}
.pill{display:inline-block;padding:2px 8px;border-radius:12px;font-size:11px;font-weight:700;background:var(--ac);color:#fff}
.posesel{padding:4px 6px;border:1px solid var(--bd);border-radius:6px;background:var(--card);color:var(--tx);font-size:12px}
.posesel.ovr{border-color:var(--ac);box-shadow:0 0 0 1px var(--ac)}
.ovrflag{font-size:10px;color:var(--ac);font-weight:700;white-space:nowrap}
.plink{text-decoration:none;font-size:13px;cursor:pointer}.plink:hover{opacity:.7}
.btn{padding:8px 10px;border:1px solid var(--bd);border-radius:8px;background:var(--card);color:var(--tx);cursor:pointer;font-size:13px}
.mailcard{border:1px solid var(--bd);border-left:5px solid var(--ac);border-radius:10px;background:var(--card);padding:12px 14px;margin:0 0 12px}
.mailhd{display:flex;flex-wrap:wrap;gap:6px 14px;align-items:center;justify-content:space-between}
.mailcov{margin:8px 0}
.mailbody{white-space:pre-wrap;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:12.5px;line-height:1.5;background:rgba(127,127,127,.06);border-radius:8px;padding:10px 12px;margin:6px 0 0;overflow-x:auto}
.gmlink{font-size:12px;font-weight:700;color:#fff;background:var(--ac);border-radius:8px;padding:5px 10px;text-decoration:none;white-space:nowrap}
.gmlink:hover{opacity:.9}
.flash{animation:fl 1.6s ease}@keyframes fl{0%,40%{box-shadow:0 0 0 3px var(--org) inset}100%{box-shadow:none}}
'''

JS = r'''
const DATA=__DATA__;
const $=s=>document.querySelector(s);
let tab="synth",q="",fp="";
// état des filtres de la table dossiers
let dq="",fFac="",fPose="",fDept="",sortCol="client",sortDir=1;
function esc(s){return (s||"").replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");}
function jsq(s){return (s||"").replace(/\\/g,"\\\\").replace(/'/g,"\\'");}

// ---- surcharges manuelles, mémorisées sur le poste ----
const OVK="audit_pose_ovr_v1";   // colonne "Posé ?"
const FAK="audit_fac_ovr_v1";    // colonne "Facturée ?"
const AFK="audit_afac_ovr_v1";   // colonne "À facturer ?"
let OVR={};try{OVR=JSON.parse(localStorage.getItem(OVK)||"{}");}catch(e){OVR={};}
let FAC={};try{FAC=JSON.parse(localStorage.getItem(FAK)||"{}");}catch(e){FAC={};}
let AF ={};try{AF =JSON.parse(localStorage.getItem(AFK)||"{}");}catch(e){AF ={};}
function dkey(x){return (x.dia&&x.dia[0])?x.dia[0]:x.client;}
function isFac(x){const k=dkey(x);if(FAC[k]=="oui")return true;if(FAC[k]=="non")return false;return !!(x.invoice&&x.invoice.trim());}
function afacOf(x){const k=dkey(x);return AF[k]||x.afac_def||"Oui";}
function recompFstat(x){
 if(isFac(x))return "Facturé";
 if(afacOf(x)=="Non")return "Hors facturation";
 if(x.pose=="Oui")return "Réalisée — NON facturée";
 if(x.pose=="Non")return (x.future||x.enc)?"En cours — pas encore posée":"Commande reçue — à vérifier";
 return "Commande reçue — à vérifier";}
function applyOvr(){DATA.dossiers.forEach(x=>{const k=dkey(x);
  x._ovr=(OVR[k]!==undefined); x._facovr=(FAC[k]!==undefined); x._afovr=(AF[k]!==undefined);
  if(x._ovr)x.pose=OVR[k];
  if(x._ovr||x._facovr||x._afovr)x.fstat=recompFstat(x);});}
applyOvr();
window.setPose=(k,v)=>{OVR[k]=v;localStorage.setItem(OVK,JSON.stringify(OVR));applyOvr();render();};
window.setFac=(k,v)=>{FAC[k]=v;localStorage.setItem(FAK,JSON.stringify(FAC));applyOvr();render();};
window.setAfac=(k,v)=>{AF[k]=v;localStorage.setItem(AFK,JSON.stringify(AF));applyOvr();render();};
window.resetOvr=()=>{if(!confirm("Annuler toutes vos corrections « Posé ? » ?"))return;OVR={};localStorage.removeItem(OVK);applyOvr();render();};
window.resetFac=()=>{if(!confirm("Annuler toutes vos saisies « Facturée ? » ?"))return;FAC={};localStorage.removeItem(FAK);applyOvr();render();};
window.resetAf =()=>{if(!confirm("Annuler toutes vos saisies « À facturer ? » ?"))return;AF={};localStorage.removeItem(AFK);applyOvr();render();};
function fcount(s){return DATA.dossiers.filter(x=>x.fstat==s).length;}
function nOvr(){return Object.keys(OVR).length;}
function nFacSaisies(){return Object.values(FAC).filter(v=>v=="oui").length;}
function nAfNon(){return Object.values(AF).filter(v=>v=="Non").length;}
window.goProof=(id)=>{tab="ev";render();setTimeout(()=>{const el=document.getElementById(id);if(el){el.scrollIntoView({behavior:"smooth",block:"start"});el.classList.remove("flash");void el.offsetWidth;el.classList.add("flash");}},60);};

function pbadge(s){const k=s.split(" ")[0];return `<span class="badge p-${k}">${s}</span>`;}
function fbadge(s){let c="f-ver";if(s=="Facturé")c="f-fac";else if(s.startsWith("Réalisée"))c="f-non";else if(s.startsWith("En cours"))c="f-enc";else if(s=="Hors facturation")c="f-off";return `<span class="badge ${c}">${s}</span>`;}
function dept(x){return (x.cp||"").toString().replace(/\s/g,'').slice(0,2)||"—";}

function proofOf(inv){const fp=(DATA.fac_proof||{});const k=(inv||"").replace("-IRSH","").trim();return fp[k]||"";}
function regTable(reg){let rows=reg;if(fp)rows=rows.filter(r=>r[3].startsWith(fp));
 return `<div class=wrap><table><thead><tr><th>N° Facture</th><th>Date</th><th>Montant €</th><th>Paiement</th><th>Preuve</th><th>Source / détail</th></tr></thead><tbody>`+
 rows.map(r=>{const pid=proofOf(r[0]);const pl=pid?`<a class=plink href="#" onclick="goProof('${pid}');return false">📎 mail</a>`:"";
   return `<tr><td><b>${r[0]}</b></td><td class=small>${r[1]}</td><td>${r[2]}</td><td>${pbadge(r[3])}</td><td>${pl}</td><td class=small>${r[4]}</td></tr>`;}).join("")+
 `</tbody></table></div><p class=small>${rows.length} lignes. 📎 = preuve mail reliée (clic). * = date antidatée (voir anomalies).</p>`;}
function payCount(reg,pre){return reg.filter(r=>r[3].startsWith(pre)).length;}
function reprBlock(k){const r=DATA.reprise[k];return `<div class="card reprise"><h3>${k}</h3>
 <div class=small>Dernière facture émise :</div><div style="margin:2px 0 8px">${r.derniere}</div>
 <div class=small>➡️ Reprendre la numérotation à :</div><div class=big>${r.repartir}</div>
 <div class=small style="margin-top:6px">Avoirs : ${r.avoir}</div>
 <div class=small style="margin-top:6px;color:var(--org-tx)">${r.note}</div></div>`;}
function synth(){const ri=DATA.reg_irsh,rb=DATA.reg_barros,fc=DATA.fstat_counts||{};
 return `<div class=kpis>
  <div class="kpi clk" onclick="goFact('')"><b>${ri.length+rb.length}</b><span>Factures/avoirs recensés →</span></div>
  <div class="kpi clk" onclick="goFact('Payée')"><b style="color:var(--grn)">${payCount(ri,'Payée')+payCount(rb,'Payée')}</b><span>Payées →</span></div>
  <div class="kpi clk" onclick="goFact('Non')"><b style="color:var(--red)">${payCount(ri,'Non')+payCount(rb,'Non')}</b><span>Non payées →</span></div>
  <div class="kpi clk" onclick="goNonFac()"><b style="color:var(--red)">${fcount('Réalisée — NON facturée')}</b><span>Posés NON facturés →</span></div>
  <div class="kpi clk" onclick="setTab('an')"><b style="color:var(--org)">${DATA.anomalies.length}</b><span>Anomalies →</span></div></div>
 <h2 style="font-size:16px;margin:6px 0">Reprise de la numérotation</h2>
 <div style="display:flex;gap:12px;flex-wrap:wrap">${reprBlock('IRSH')}${reprBlock('BARROS')}</div>
 <div class=card><b>Comment lire l'état de paiement</b><div class=small style="margin-top:6px">
 Source IRSH : mails de la compta IRSH (Camille Bustreau, le plus récent 09/07/2026) + point compta 17/04 + envois de factures. Source BARROS : détail des virements Eco Shower (19/05) + Qonto.<br>
 <span class="badge p-Payée">Payée</span> · <span class="badge p-Non">Non payée</span> · <span class="badge p-À">À vérifier</span> · <span class="badge p-Avoir">Avoir</span></div></div>`;}
function anom(){return DATA.anomalies.map(a=>{const c={CRITIQUE:'rc',ÉLEVÉE:'ro',MOYENNE:'rb',INFO:'rm'}[a.sev];
 return `<div class="an sev-${a.sev}"><span class="lab ${c}">${a.sev}</span><h3>${a.titre}</h3>
 <div class=small><b>Preuve :</b> ${a.preuve}</div><div style="margin-top:4px"><b>Constat :</b> ${a.constat}</div></div>`;}).join("");}
function evid(){
 const pc=(DATA.proofs||[]).map(p=>`<div class=mailcard id="${p.id}">
   <div class=mailhd><div><b>${esc(p.subj)}</b><div class=small>${esc(p.from)} · ${esc(p.date)}</div></div>
     <a class=gmlink href="${p.gmail}" target=_blank rel="noopener noreferrer">Ouvrir dans Gmail ↗</a></div>
   <div class=mailcov>Factures prouvées : ${p.covers.map(c=>`<span class=chip>${c}</span>`).join(" ")}</div>
   <pre class=mailbody>${esc(p.body)}</pre></div>`).join("");
 const ev=DATA.evidence.map(e=>`<div class=ev><div class=m>${e.date} · ${e.from} · <i>${e.subj}</i></div>${e.detail}</div>`).join("");
 return `<div class=note>📎 Les cartes ci-dessous sont les <b>mails qui prouvent le rattachement facture → chantier</b>. Le bouton « Ouvrir dans Gmail » ouvre le mail d'origine dans votre boîte.</div>`+pc+
   `<h3 style="margin:16px 0 6px;font-size:15px">Autres évènements de facturation</h3>`+ev;}

// ---------- Table Dossiers, filtrable + triable par colonne ----------
window.setFilt=(k,v)=>{if(k=='dq')dq=v;if(k=='fac')fFac=v;if(k=='pose')fPose=v;if(k=='dept')fDept=v;render();};
window.setSort=c=>{if(sortCol==c)sortDir=-sortDir;else{sortCol=c;sortDir=1;}render();};
window.resetFilt=()=>{dq="";fFac="";fPose="";fDept="";render();};
window.goNonFac=()=>{tab="do";fFac="Réalisée — NON facturée";fPose="";fDept="";dq="";render();window.scrollTo(0,0);};
window.goFact=(f)=>{tab="fi";fp=f;render();window.scrollTo(0,0);};

function dossFiltered(){let d=[...DATA.dossiers];const Q=dq.toLowerCase();
 if(dq)d=d.filter(x=>x.client.toLowerCase().includes(Q)||x.dia.join(" ").toLowerCase().includes(Q)||(x.invoice||"").toLowerCase().includes(Q));
 if(fFac)d=d.filter(x=>x.fstat==fFac);
 if(fPose)d=d.filter(x=>x.pose==fPose);
 if(fDept)d=d.filter(x=>dept(x)==fDept);
 const key=x=>({client:x.client,dia:(x.dia[0]||""),dept:dept(x),rdv:(x.rdv||""),crm:x.crm_status||"",fac:x.invoice||"",afac:afacOf(x),stat:x.fstat,pose:x.pose}[sortCol]||"");
 d.sort((a,b)=>{const A=key(a).toString().toUpperCase(),B=key(b).toString().toUpperCase();return A<B?-sortDir:A>B?sortDir:0;});
 return d;}

function ar(c){return sortCol==c?`<span class=ar>${sortDir>0?'▲':'▼'}</span>`:'<span class=ar>↕</span>';}
function opts(sel,arr){return arr.map(v=>`<option ${sel==v?'selected':''}>${v}</option>`).join("");}

function dossTable(nonfacView){
 const depts=[...new Set(DATA.dossiers.map(dept))].filter(x=>x!="—").sort();
 const fstats=["Facturé","Réalisée — NON facturée","En cours — pas encore posée","Commande reçue — à vérifier","Hors facturation"];
 let head=`<div class=kpis>`+fstats.map(s=>{const on=fFac==s?'on':'';const col=s=='Facturé'?'grn':s.startsWith('Réalisée')?'red':s.startsWith('En cours')?'blu':s=='Hors facturation'?'mut':'org';
   return `<div class="kpi clk ${on}" onclick="setFilt('fac','${fFac==s?'':s}')"><b style="color:var(--${col})">${fcount(s)}</b><span>${s}</span></div>`;}).join("")+`</div>`;
 let ovrn=nOvr();
 let ctl=`<div class=ctl>
   <input type=text placeholder="Rechercher nom de chantier / DIA / facture…" value="${dq}" oninput="setFilt('dq',this.value)">
   <select onchange="setFilt('fac',this.value)"><option value="">Statut : tous</option>${opts(fFac,fstats)}</select>
   <select onchange="setFilt('pose',this.value)"><option value="">Pose : toutes</option>${opts(fPose,["Oui","Non","À vérifier"])}</select>
   <select onchange="setFilt('dept',this.value)"><option value="">Dépt : tous</option>${opts(fDept,depts)}</select>
   <button class=btn onclick="resetFilt()">Réinitialiser filtres</button>
   ${ovrn?`<button class=btn onclick="resetOvr()" title="Annuler vos corrections manuelles">↩︎ ${ovrn} correction(s) « Posé »</button>`:""}
   ${nFacSaisies()?`<button class=btn onclick="resetFac()" title="Annuler vos saisies Facturée">↩︎ ${nFacSaisies()} « Facturée » saisie(s)</button>`:""}
   ${nAfNon()?`<button class=btn onclick="resetAf()" title="Annuler vos saisies À facturer">↩︎ ${nAfNon()} « Hors facturation »</button>`:""}
 </div>`;
 const d=dossFiltered();
 const cols=[["client","Nom de chantier"],["dia","N° DIA"],["dept","Dépt"],["rdv","RDV pose"],["crm","CRM (Compiexe)"],["afac","À facturer ?"],["fac","Facture rattachée"],["stat","Statut facturation"],["pose","Posé ?"]];
 let thead=`<tr>`+cols.map(([k,l])=>`<th class=sortable onclick="setSort('${k}')">${l} ${ar(k)}</th>`).join("")+`</tr>`;
 const poseSel=x=>{const k=jsq(dkey(x));const cur=x.pose||"À vérifier";
   return `<select class="posesel${x._ovr?' ovr':''}" onchange="setPose('${k}',this.value)">`+
     ["Oui","Non","À vérifier"].map(v=>`<option ${cur==v?'selected':''}>${v}</option>`).join("")+
     `</select>${x._ovr?' <span class=ovrflag>modifié</span>':''}`;};
 const facSel=x=>{const k=jsq(dkey(x));const f=isFac(x);
   return `<select class="posesel${x._facovr?' ovr':''}" onchange="setFac('${k}',this.value)">`+
     `<option value="oui" ${f?'selected':''}>Oui</option><option value="non" ${!f?'selected':''}>Non</option>`+
     `</select>`;};
 const afacSel=x=>{const k=jsq(dkey(x));const cur=afacOf(x);
   return `<select class="posesel${x._afovr?' ovr':''}" onchange="setAfac('${k}',this.value)">`+
     ["Oui","Non","À vérifier"].map(v=>`<option ${cur==v?'selected':''}>${v}</option>`).join("")+
     `</select>`;};
 let body=d.map(x=>{const pid=x.proof||proofOf(x.invoice);
   const ref=x.invoice?`<b>${x.invoice}</b>${pid?` <a class=plink href="#" onclick="goProof('${pid}');return false" title="Voir la preuve">📎</a>`:""}`:"";
   const facCell=`<div>Facturée ? ${facSel(x)}</div>${ref?`<div class=small style="margin-top:2px">${ref}</div>`:""}`;
   return `<tr>
   <td><b>${x.client}</b>${x.pose_src?`<div class=small>${x.pose_src}</div>`:""}</td>
   <td>${x.dia.map(r=>`<span class=chip>${r}</span>`).join(" ")||"—"}</td>
   <td class=small>${dept(x)}</td>
   <td class=small>${x.rdv||"—"}</td>
   <td class=small>${x.in_crm?(x.crm_type?x.crm_type+" · ":"")+ (x.crm_status||""):"—"}</td>
   <td>${afacSel(x)}</td>
   <td>${facCell}</td>
   <td>${fbadge(x.fstat)}</td>
   <td>${poseSel(x)}</td></tr>`;}).join("");
 const restant=fcount("Réalisée — NON facturée"), faites=nFacSaisies();
 let progress = nonfacView ? `<div class=card style="border-left:5px solid var(--grn)"><b>Avancement facturation</b> — ✔️ <b style="color:var(--grn)">${faites}</b> facture(s) que vous avez saisie(s) · reste <b style="color:var(--red)">${restant}</b> à faire. <span class=small>Passez « Facturée ? » à <b>Oui</b> quand vous éditez la facture : la ligne bascule en vert et sort de cette liste.</span></div>` : "";
 let intro = nonfacView ? progress+`<div class=note><b>⚠️ Dossiers posés (installés) mais NON facturés</b> — <b>règle appliquée : dès que la date de RDV pose est passée, l'intervention est considérée réalisée</b> (les statuts de l'export ne sont pas à jour). Croisé avec le CRM Compiexe à jour (${DATA.crm_asof||''}) et les mails. Ce sont les dossiers à facturer en priorité (reprise à <b>F2026-25</b>). ⚠️ Vérifiez le <b>type</b> (colonne CRM) : SAV/REWORK ne sont pas toujours facturables comme une pose. Cliquez une colonne pour trier. <b>Colonnes modifiables</b> (mémorisées sur votre poste) : « <b>Posé ?</b> » si Compiexe se trompe · « <b>À facturer ?</b> » passez à <b>Non</b> pour exclure un dossier (SAV dont on est responsable, DIA à 0€…) → il passe en « Hors facturation » · « <b>Facturée ?</b> » = Oui quand la facture est faite.</div>` : "";
 return head+intro+ctl+`<div class=wrap><table><thead>${thead}</thead><tbody>${body}</tbody></table></div>
   <p class=small>${d.length} dossier(s) affiché(s) sur ${DATA.dossiers.length}. Rapprochement : <b>N° DIA → nom de chantier → facture</b> (source mails IRSH + CRM Compiexe ; le fichier de suivi n'est pas utilisé comme référence).</p>`;}

const T=[["synth","Synthèse & Reprise"],["nf","⚠️ Non facturés"],["do","Dossiers (tous)"],["fi","Factures IRSH"],["fb","Factures BARROS"],["an","Anomalies"],["ev","Preuves (mails)"]];
window.setTab=k=>{if(k=="nf"){tab="do";fFac="Réalisée — NON facturée";fPose="";fDept="";dq="";}else{tab=k;fp="";}render();};

function payFilter(){return `<div class=ctl><select onchange="fp=this.value;render()">
 <option value="">— Tout paiement —</option><option value="Payée" ${fp=='Payée'?'selected':''}>Payées</option>
 <option value="Non" ${fp=='Non'?'selected':''}>Non payées</option><option value="À" ${fp=='À'?'selected':''}>À vérifier</option>
 <option value="Avoir" ${fp=='Avoir'?'selected':''}>Avoirs</option></select></div>`;}

function render(){let b="";
 const nonfacView=(tab=="do" && fFac=="Réalisée — NON facturée");
 const curTab = nonfacView ? "nf" : tab;
 if(tab=="synth")b=synth();
 else if(tab=="do")b=dossTable(nonfacView);
 else if(tab=="fi")b=`<h2 style="font-size:16px">Factures IRSH → Indépendance Royale</h2>`+payFilter()+regTable(DATA.reg_irsh);
 else if(tab=="fb")b=`<h2 style="font-size:16px">Factures BARROS / Eco Shower</h2>`+payFilter()+regTable(DATA.reg_barros);
 else if(tab=="an")b=anom();
 else if(tab=="ev")b=`<p class=small>Événements de facturation retrouvés dans les boîtes mail (source de vérité).</p>`+evid();
 $("#app").innerHTML=`<h1>Audit Facturation 2026 — ETS OUHADDAD</h1>
 <p class=sub>IRSH (Indépendance Royale) + BARROS (Eco Shower) · généré ${DATA.generated} · sources : boîtes mail + CRM Compiexe (le fichier de suivi n'est pas la référence)</p>
 <div class=tabs>${T.map(([k,l])=>`<div class="tab ${curTab==k?'on':''} ${k=='nf'?'alert':''}" onclick="setTab('${k}')">${l}</div>`).join("")}</div>`+b;}
render();
'''

html = '<div id="app"></div>\n<style>' + CSS + '</style>\n<script>' + JS.replace("__DATA__", DATA) + '</script>'
open("audit/Audit_Factures_outil.html", "w", encoding="utf-8").write(html)
print("HTML v3 écrit:", len(html), "octets")
