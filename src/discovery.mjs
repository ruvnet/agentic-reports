import {z} from 'zod';import {digest,generateReport} from './reports.mjs';
const querySchema=z.object({topic:z.string().min(1).max(512)}).strict();
// CLI-only capability. Never registered with MCP; endpoint cannot be supplied by a caller.
export async function discover(input,{env=process.env,fetchImpl=fetch,timeoutMs=10000}={}){
 const {topic}=querySchema.parse(input);
 if(env.REPORTS_ALLOW_NETWORK!=='1'||!env.EXA_API_KEY||env.EXA_API_KEY.length<16||env.EXA_API_KEY.length>512)throw Error('Provider capability disabled');
 const domains=(env.REPORTS_EXA_DOMAINS||'').split(',').map(s=>s.trim().toLowerCase());
 if(!domains.length||domains.length>10||domains.some(d=>! /^(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,63}$/.test(d)))throw Error('Explicit domain allowlist required');
 const abort=new AbortController();let reader;const timer=setTimeout(()=>abort.abort(),timeoutMs);
 const bounded=async promise=>{let listener;try{return await Promise.race([promise,new Promise((_,reject)=>{listener=()=>reject(Error('Deadline'));if(abort.signal.aborted)listener();else abort.signal.addEventListener('abort',listener,{once:true});})]);}finally{if(listener)abort.signal.removeEventListener('abort',listener);}};
 try{
  const res=await bounded(fetchImpl('https://api.exa.ai/search',{method:'POST',redirect:'error',signal:abort.signal,headers:{'content-type':'application/json','x-api-key':env.EXA_API_KEY},body:JSON.stringify({query:topic,numResults:5,includeDomains:domains,contents:{text:{maxCharacters:8192}}})}));
  if(!res.ok||!res.body)throw Error('Provider rejected request');
  reader=res.body.getReader();let bytes=0,frames=0;const chunks=[];
  while(true){const {done,value}=await bounded(reader.read());if(done)break;bytes+=value.length;if(bytes>128*1024||++frames>4096)throw Error('Provider output budget exceeded');chunks.push(Buffer.from(value));}
  const body=JSON.parse(Buffer.concat(chunks).toString('utf8'));
  if(!Array.isArray(body.results)||body.results.length<1||body.results.length>5)throw Error('Invalid results');
  const now=new Date().toISOString();const sources=body.results.map(s=>{const u=new URL(s.url);if(!domains.some(d=>u.hostname===d||u.hostname.endsWith('.'+d)))throw Error('Provider returned disallowed domain');return {id:'s'+digest(s.url).slice(0,24),url:s.url,title:s.title,text:s.text,capturedAt:now,...(s.publishedDate?{publishedAt:s.publishedDate}:{})};});
  return generateReport({topic,asOf:now,sources});
 }catch{throw Error('Provider discovery failed; no report produced');}finally{clearTimeout(timer);abort.abort();if(reader)void reader.cancel().catch(()=>{});}
}
