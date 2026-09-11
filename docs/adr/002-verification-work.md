# ADR 002: Reduce verification work without retaining private evidence

Status: accepted. 2026-09-11.

The original verifier fully regenerated a report, including its canonical integrity hash, and then canonicalized both the submitted and regenerated report again to compare them. This performed two additional recursive key sorting and serialization passes across all snapshots and quotes.

Use Node's `isDeepStrictEqual` on the submitted and fully regenerated report. All source validation, freshness checks, BM25 retrieval, quote construction and hash generation still run. Object key order remains irrelevant; array order, values, types and extra properties remain checked. Canonical report bytes and hashes are unchanged. Noncanonical in-memory objects such as unusual prototypes may be rejected more strictly. Public CLI and MCP inputs are JSON.

No cross-request cache, retained source index, validation shortcut or trusted caller hash is introduced. Source limits remain 100 documents and 128 KiB per request. The comparison benchmarks 100 sources in one request and 1000 sources as ten independent bounded requests.

The measurement uses the merged baseline `4702b5124aa3740e2d868f62dad86caef6fd00b8`, 30 warmup pairs, seven repetitions of 50 alternating baseline/candidate iterations, and immutable inputs. Forty additional fixture cases compare every report field and citation result, exercise key reordering and reject extra report data. Timings include full verification, not comparison alone. CI retains raw repetitions; latency is evidence, not a flaky absolute pass gate.

[AMA-Bench v4](https://arxiv.org/abs/2602.22769v4) studies objective and causal information in agent memory and identifies limitations of similarity-only retrieval. Its relevance here is to preserve complete evidence and provenance while optimizing computation. We did not reproduce its benchmark, implement its causal graph system, or claim its performance. The retrieval kernel remains BM25, not a causal reasoner.

[Node's official documentation](https://nodejs.org/api/util.html#utilisdeepstrictequalval1-val2-options) describes the built-in strict deep comparison. This change uses its default prototype checking and is validated on Node 24.

Acceptance: every baseline/candidate fixture report, hash and citation result matches; nested key reordering verifies; altered types, quote spans, extra properties and stale source membership are rejected. Domain tests and actual SDK subprocess tests remain passing.
