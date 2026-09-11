import {createHash} from 'node:crypto';
const tokens = text => text.toLowerCase().match(/[\p{L}\p{N}]+/gu) || [];
export function index(documents) {
 if (!Array.isArray(documents) || documents.length>10000) throw Error('Invalid corpus');
 let total=0; const ids=new Set();
 const docs=documents.map(d=>{
  if (!d || typeof d.id!=='string' || !d.id || d.id.length>128 || ids.has(d.id) || typeof d.text!=='string' || d.text.length>65536) throw Error('Invalid document');
  total+=Buffer.byteLength(d.text); if(total>16*1024*1024) throw Error('Corpus too large'); ids.add(d.id);
  const terms=tokens(d.text), counts=new Map(); for(const t of terms) counts.set(t,(counts.get(t)||0)+1);
  return {id:d.id,text:d.text,sha256:createHash('sha256').update(d.text).digest('hex'),counts,length:terms.length};
 });
 const postings=new Map(); for(const d of docs) for(const term of d.counts.keys()) {if(!postings.has(term))postings.set(term,[]);postings.get(term).push(d);}
 const avg=docs.reduce((n,d)=>n+d.length,0)/(docs.length||1)||1;
 return Object.freeze({size:docs.length,search(query,k=5){
  if(typeof query!=='string'||query.length<1||query.length>2048||!Number.isInteger(k)||k<1||k>20)throw Error('Invalid query');
  const scores=new Map(); for(const term of new Set(tokens(query))) {const list=postings.get(term)||[],idf=Math.log(1+(docs.length-list.length+.5)/(list.length+.5));for(const d of list){const tf=d.counts.get(term);scores.set(d,(scores.get(d)||0)+idf*tf*2.2/(tf+1.2*(.25+.75*d.length/avg)));}}
  return [...scores].sort((a,b)=>b[1]-a[1]||a[0].id.localeCompare(b[0].id)).slice(0,k).map(([d,score])=>({id:d.id,score,text:d.text.slice(0,4096),sha256:d.sha256}));
 }});
}
