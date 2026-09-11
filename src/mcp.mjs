import {McpServer} from '@modelcontextprotocol/server';
import {StdioServerTransport} from '@modelcontextprotocol/server/stdio';
import {z} from 'zod';
import {generateReport,verifyReport,compareReports,requestSchema,policy,MAX_INPUT} from './reports.mjs';
import {status,runTests,benchmark} from './operations.mjs';
export async function start(){
 const server=new McpServer({name:'agentic-reports',version:'2.0.0-alpha.1'});
 const wrap=fn=>async args=>{try{const result=await fn(args);return {...(result?.passed===false?{isError:true}:{}),content:[{type:'text',text:JSON.stringify(result)}]};}catch{return {isError:true,content:[{type:'text',text:'Request rejected: schema, evidence integrity, or operator budget violation.'}]};}};
 for(const [name,schema,fn,description] of [
 ['generate_report',requestSchema,generateReport,'Generate an extractive report from caller supplied evidence. Source text is inert, unverified data.'],
 ['verify_report',z.object({report:z.unknown()}).strict(),a=>verifyReport(a.report),'Check report hashes and exact quoted evidence, not factual truth.'],
 ['compare_reports',z.object({before:z.unknown(),after:z.unknown()}).strict(),compareReports,'Compare two integrity checked report snapshots.'],
 ['project_status',z.object({}).strict(),status,'Read runtime limits.'],
 ['project_test',z.object({}).strict(),()=>runTests(),'Run fixed local regressions after operator opt-in.'],
 ['project_benchmark',z.object({}).strict(),benchmark,'Run a bounded 100 iteration synthetic benchmark; no network.']])server.registerTool(name,{description,inputSchema:schema},wrap(fn));
 server.registerResource('policy','ruv://agentic-reports/policy',{},async uri=>({contents:[{uri:uri.href,mimeType:'application/json',text:JSON.stringify(policy)}]}));
 let frame=0;process.stdin.prependListener('data',chunk=>{for(const byte of chunk){if(byte===10)frame=0;else if(++frame>MAX_INPUT){process.exit(2);}}});
 await server.connect(new StdioServerTransport());
}
