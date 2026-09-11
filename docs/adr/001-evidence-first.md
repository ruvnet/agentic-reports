# ADR 001: Evidence first report generation

Status: accepted for v2 alpha. Reviewed 2026-09-11.

## Problem

The historical Python service exposed paid provider operations without an authentication boundary. Model responses supplied citations that were not checked against evidence; request fanout, long provider timeouts and console logging also enlarged privacy and cost risk. The old start scripts installed packages and prompted for keys while starting a public listener.

## Decision

Replace the supported entry point with an explicit local Node CLI and official MCP SDK v2 stdio service. Retire old launchers before imports, credential prompts or installs. Generate extractive reports with actual Agentic Search BM25 source pinned to upstream aa2662dc082cd0d6cc502aaebbc16230f7a3a220. Preserve its MIT license and source checksum. No learned retrieval quality is claimed.

Each report owns its snapshots and exact quoted passages. Canonical JSON hashing and deterministic regeneration check integrity, schema and citation membership. All documents remain caller supplied and unauthenticated. A hash is not a signature or proof of truth. Compare reports only after checking both and requiring equal topics. `asOf` is an explicit replay parameter, not trusted wall clock evidence.

MCP exposes six bounded local operations and a policy resource, never a shell, filesystem path or provider endpoint. An operator can explicitly enable fixed subprocess regressions. An optional CLI only Exa adapter calls one fixed HTTPS endpoint, restricts result domains and applies deadline, byte and result budgets. No retries, LLM synthesis, remote writes or automatic promotion are enabled.

## Alternatives

Keeping the old service would require a complete multiuser identity, cost accounting and provider execution redesign. Adding vector search now would increase dependencies before a representative retrieval evaluation exists. Treating model generated citations as evidence would conceal the central correctness problem. This release deliberately supports verifiable excerpts while those broader capabilities remain deployment qualification work.

## Research and provenance

* [Official SDK](https://github.com/modelcontextprotocol/typescript-sdk): v2 split server/client packages, stdio transport and Standard Schema tool validation. Pinned installed SDK 2.0.0 and Zod 4.3.6.
* [Agentic Search source](https://github.com/ruvnet/agentic-search/blob/aa2662dc082cd0d6cc502aaebbc16230f7a3a220/src/search.js): BM25 postings and source SHA256. This exact file is vendored under MIT.
* [Exa Search reference](https://exa.ai/docs/reference/search): fixed POST search endpoint, result count, domain selection and returned text. The adapter's contract was checked against this reference; live service behavior remains unqualified.

These sources inform concrete interfaces, not a SOTA superiority claim.

## Acceptance

Real CLI and official MCP client subprocesses generate and verify identical reports. Tampered quotes, stale and future evidence, duplicate IDs, oversized input, unknown operations and unauthorized provider calls are rejected. CI reruns tests, dependency audit, fixtures and release packaging. Production source acquisition authenticity, deployment isolation and account budget enforcement remain operator responsibilities.
