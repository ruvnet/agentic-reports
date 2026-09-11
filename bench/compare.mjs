// Reproduce against the reviewed merged baseline; no network or private corpus.
import {execFileSync} from 'node:child_process';
import {writeFileSync,unlinkSync} from 'node:fs';
import {randomUUID} from 'node:crypto';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {isDeepStrictEqual} from 'node:util';
import * as candidate from '../src/reports.mjs';
const root=fileURLToPath(new URL('../',import.meta.url));
const baselineCommit='4702b5124aa3740e2d868f62dad86caef6fd00b8';
const baselinePath=root+'.benchmark-baseline-'+randomUUID()+'.mjs';
const source=execFileSync('git',['show',baselineCommit+':src/reports.mjs'],{cwd:root,encoding:'utf8',maxBuffer:65536}).replace("'../vendor/agentic-search/search.js'","'./vendor/agentic-search/search.js'");
writeFileSync(baselinePath,source,{mode:0o600,flag:'wx'});
try {
 const baseline=await import(pathToFileURL(baselinePath).href);
 const request=Object.freeze({topic:'evidence security',asOf:'2026-09-11T00:00:00Z',limit:20,maxAgeDays:30,sources:Object.freeze(Array.from({length:100},(_,i)=>Object.freeze({id:'s'+i,title:'Synthetic source '+i,url:'https://example.com/'+i,capturedAt:'2026-09-10T00:00:00Z',text:('evidence security objective capture provenance '+i+' ').repeat(14)})))});
 const immutable=JSON.stringify(request),report=candidate.generateReport(request);const original=JSON.stringify(report);
 if(!isDeepStrictEqual(report,baseline.generateReport(request)))throw Error('Citation or report output mismatch');
 const equivalenceCases=40;
 for(let i=0;i<equivalenceCases;i++){
  const varied={...request,topic:i%4===0?'absent':i%3===0?'objective':'security',limit:i%20+1,maxAgeDays:i%2?0:30,sources:request.sources.slice(0,i%100+1)};
  const expected=baseline.generateReport(varied),actual=candidate.generateReport(varied);
  if(!isDeepStrictEqual(actual,expected)||!isDeepStrictEqual(candidate.verifyReport(actual),baseline.verifyReport(actual)))throw Error('Varied citation result mismatch');
  // Reordered object keys stay valid; any new top level data remains invalid.
  const reordered=Object.fromEntries(Object.entries(actual).reverse());
  if(!candidate.verifyReport(reordered).valid)throw Error('Object order changed acceptance');
  const tampered={...actual,unexpected:true};
  for(const engine of [baseline,candidate]){let rejected=false;try{engine.verifyReport(tampered);}catch{rejected=true;}if(!rejected)throw Error('Unknown report data accepted');}
 }
 const q=(xs,p)=>xs.slice().sort((a,b)=>a-b)[Math.ceil(xs.length*p)-1];
 const results=[];
 for(const batch of [1,10]){
  const run=engine=>{for(let n=0;n<batch;n++){const receipt=engine.verifyReport(report);if(!receipt.valid||receipt.sha256!==report.sha256)throw Error('Invalid receipt');}};
  for(let i=0;i<30;i++){run(baseline);run(candidate);}
  const reps=[];
  for(let rep=0;rep<7;rep++){
   const a=[],b=[];
   // Alternate order to reduce warmup and machine drift bias.
   for(let i=0;i<50;i++){for(const name of ((i+rep)%2?['candidate','baseline']:['baseline','candidate'])){const begin=performance.now();run(name==='baseline'?baseline:candidate);(name==='baseline'?a:b).push(performance.now()-begin);}}
   reps.push({repetition:rep+1,baselineMedianMs:q(a,.5),candidateMedianMs:q(b,.5),baselineP95Ms:q(a,.95),candidateP95Ms:q(b,.95)});
  }
  results.push({sources:100*batch,requestsPerIteration:batch,sourcesPerRequest:100,iterationsPerRepetition:50,warmupPairs:30,repetitions:reps,medianOfP95BaselineMs:q(reps.map(r=>r.baselineP95Ms),.5),medianOfP95CandidateMs:q(reps.map(r=>r.candidateP95Ms),.5)});
 }
 if(JSON.stringify(request)!==immutable||JSON.stringify(report)!==original)throw Error('Input mutated');
 console.log(JSON.stringify({baselineCommit,node:process.version,platform:process.platform,arch:process.arch,fixture:true,allCitationResultsEquivalent:true,equivalenceCases,inputUnmodified:true,scope:'Verification; 1000 sources are ten independent bounded100-source reports',results},null,2));
}finally{unlinkSync(baselinePath);}
