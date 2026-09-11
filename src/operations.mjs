import {spawn} from 'node:child_process';
import {fileURLToPath} from 'node:url';
import {digest,policy,generateReport} from './reports.mjs';
const root=fileURLToPath(new URL('../',import.meta.url));
let running=false;
export function status(){return {project:'agentic-reports',version:'2.0.0-alpha.1',...policy};}
export function runTests({allowed=process.env.REPORTS_ALLOW_VALIDATION==='1'}={}){
 if(!allowed)throw Error('Operator must enable REPORTS_ALLOW_VALIDATION=1');
 if(running)throw Error('Validation busy');running=true;
 return new Promise((resolve,reject)=>{let bytes=0,output='',failed=false;const child=spawn(process.execPath,['--test','tests/reports.test.mjs','tests/discovery.test.mjs'],{cwd:root,env:{PATH:process.env.PATH||''},stdio:['ignore','pipe','pipe'],detached:process.platform!=='win32'});
 const kill=()=>{try{process.platform==='win32'?child.kill('SIGKILL'):process.kill(-child.pid,'SIGKILL');}catch{}};
 const timer=setTimeout(()=>{failed=true;kill();},30000);
 for(const stream of [child.stdout,child.stderr])stream.on('data',chunk=>{bytes+=chunk.length;if(bytes>65536){failed=true;kill();}else output+=chunk.toString();});
 child.on('error',()=>{clearTimeout(timer);running=false;reject(Error('Validation failed to start'));});
 child.on('close',code=>{clearTimeout(timer);running=false;failed?reject(Error('Validation exceeded budget')):resolve({passed:code===0,exitCode:code,outputSha256:digest(output),bytes,signed:false,automaticPromotion:false});});
 });
}
export function benchmark(){
 const sources=Array.from({length:100},(_,i)=>({id:'s'+i,title:'Fixture '+i,url:'https://example.com/'+i,capturedAt:'2026-09-01T00:00:00Z',text:'Evidence report fixture retrieval security '+i}));
 const req={topic:'retrieval security',asOf:'2026-09-02T00:00:00Z',sources,limit:5};
 for(let i=0;i<10;i++)generateReport(req);
 const ms=[];let claims=0;for(let i=0;i<100;i++){const start=performance.now();claims+=generateReport(req).claims.length;ms.push(performance.now()-start);}ms.sort((a,b)=>a-b);
 return {fixture:true,iterations:100,sources:100,claims,medianMs:ms[50],p95Ms:ms[95],liveProvider:false,costUSD:0,qualityClaim:'exact quotes only; no truth or semantic evaluation'};
}
