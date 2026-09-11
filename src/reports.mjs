import {createHash} from 'node:crypto';
import {z} from 'zod';
import {index} from '../vendor/agentic-search/search.js';
export const canonical = value => JSON.stringify(value, (_,v)=>v && typeof v==='object' && !Array.isArray(v) ? Object.fromEntries(Object.keys(v).sort().map(k=>[k,v[k]])) : v);
export const digest = value => createHash('sha256').update(typeof value === 'string' ? value : canonical(value)).digest('hex');
const boundedText=(max)=>z.string().min(1).max(max).refine(s=>!/[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/u.test(s),'Control characters prohibited');
const timestamp=z.string().datetime({offset:true});
const sourceSchema=z.object({id:z.string().regex(/^[a-zA-Z0-9_]{1,64}$/),title:boundedText(256),url:z.string().max(2048).url().refine(s=>{const u=new URL(s);return u.protocol==='https:'&&!u.username&&!u.password&&!u.hash;},'HTTPS metadata only'),capturedAt:timestamp,publishedAt:timestamp.optional(),text:boundedText(16384)}).strict();
export const requestSchema=z.object({topic:boundedText(512),asOf:timestamp,maxAgeDays:z.number().int().min(0).max(3650).default(30),limit:z.number().int().min(1).max(20).default(5),sources:z.array(sourceSchema).min(1).max(100)}).strict();
export const MAX_INPUT=512*1024;
export function parseInput(text){if(Buffer.byteLength(text)>MAX_INPUT)throw Error('Input exceeds 512 KiB');return JSON.parse(text);}
export function generateReport(input){
 if(Buffer.byteLength(JSON.stringify(input))>128*1024)throw Error('Evidence exceeds 128 KiB');
 const req=requestSchema.parse(input), asOf=Date.parse(req.asOf), ids=new Set();
 const snapshots=req.sources.map(s=>{
  if(ids.has(s.id))throw Error('Duplicate source ID');ids.add(s.id);
  if(Date.parse(s.capturedAt)>asOf||s.publishedAt&&Date.parse(s.publishedAt)>Date.parse(s.capturedAt))throw Error('Source timestamp is in the future');
  return {id:s.id,title:s.title,url:s.url,capturedAt:s.capturedAt,...(s.publishedAt?{publishedAt:s.publishedAt}:{}),text:s.text,sha256:digest(s.text)};
 }).sort((a,b)=>a.id<b.id?-1:a.id>b.id?1:0);
 const eligible=snapshots.filter(s=>asOf-Date.parse(s.capturedAt)<=req.maxAgeDays*86400000);
 const engine=index(eligible.map(s=>({id:s.id,text:s.text})));
 const ranked=engine.search(req.topic,req.limit);
 const claims=ranked.map((hit,i)=>({number:i+1,sourceId:hit.id,sourceSha256:hit.sha256,quote:hit.text,start:0,end:hit.text.length}));
 const payload={schemaVersion:2,topic:req.topic,asOf:req.asOf,maxAgeDays:req.maxAgeDays,limit:req.limit,method:'extractive-bm25',authenticity:'caller-supplied-unverified',snapshots,claims,excludedStale:snapshots.filter(s=>!eligible.includes(s)).map(s=>s.id)};
 return {...payload,sha256:digest(payload)};
}
export function verifyReport(report){
 if(!report||typeof report!=='object'||Array.isArray(report)||Buffer.byteLength(JSON.stringify(report))>MAX_INPUT*2)throw Error('Invalid report');
 const expected=generateReport({topic:report.topic,asOf:report.asOf,maxAgeDays:report.maxAgeDays,limit:report.limit,sources:report.snapshots?.map(({sha256,...s})=>s)});
 // Regeneration checks quoted spans, hashes, exact schema and deterministic ordering.
 if(canonical(report)!==canonical(expected))throw Error('Report integrity or evidence mismatch');
 return {valid:true,sha256:expected.sha256,claims:expected.claims.length,authenticityVerified:false};
}
export function compareReports(input){
 if(!input||Object.keys(input).sort().join(',')!=='after,before')throw Error('Expected before and after');
 const {before,after}=input;verifyReport(before);verifyReport(after);
 if(before.topic!==after.topic)throw Error('Topics differ');
 const old=new Map(before.snapshots.map(s=>[s.id,s])), next=new Map(after.snapshots.map(s=>[s.id,s]));
 return {before:before.sha256,after:after.sha256,added:[...next.keys()].filter(id=>!old.has(id)),removed:[...old.keys()].filter(id=>!next.has(id)),changed:[...next.keys()].filter(id=>old.has(id)&&digest(old.get(id))!==digest(next.get(id))),claimsChanged:digest(before.claims)!==digest(after.claims),policyChanged:before.maxAgeDays!==after.maxAgeDays||before.limit!==after.limit,asOfChanged:before.asOf!==after.asOf};
}
const esc=s=>s.replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
export function renderHtml(report){verifyReport(report);return '<!doctype html><meta charset="utf-8"><meta http-equiv="Content-Security-Policy" content="default-src &#39;none&#39;; style-src &#39;none&#39;; base-uri &#39;none&#39;"><title>'+esc(report.topic)+'</title><h1>'+esc(report.topic)+'</h1><p>Extractive evidence report. Caller supplied sources. Hashes check integrity, not truth.</p>'+report.claims.map(c=>{const s=report.snapshots.find(s=>s.id===c.sourceId);return '<article><h2>'+esc(s.title)+'</h2><blockquote>'+esc(c.quote)+'</blockquote><p>Source '+c.number+': '+esc(s.url)+'</p><p>Captured '+esc(s.capturedAt)+'; SHA256 '+c.sourceSha256+'</p></article>';}).join('')+'<p>Report SHA256 '+report.sha256+'</p>';}
export const policy=Object.freeze({network:false,storage:'request-local',sources:'caller-supplied-unverified',algorithm:'Agentic Search BM25',inputBytes:MAX_INPUT,sourceLimit:100,sourceTextCharacters:16384,maxClaims:20,commands:'fixed only',automaticPromotion:false,identity:'stdio host principal',remoteWrites:false});
