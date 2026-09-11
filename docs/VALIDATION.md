# Reproducible validation

Run on Node 24 with `npm ci --ignore-scripts`, `npm test`, `npm audit --audit-level=moderate` and `npm run benchmark`.

The suite exercises real CLI processes and official SDK MCP subprocesses, source tampering, stale/future times, duplicates, metadata validation, input and response budgets, report comparison, request isolation, HTML escaping, retired Python launchers, provider capability denial, domain enforcement and stalled body cancellation. Provider tests use controlled response fixtures. There was no paid provider request.

The benchmark warms ten iterations, then builds and queries 100 synthetic sources 100 times. It measures the complete local report construction including snapshots, BM25 selection and canonical hashing. Exact results are in evidence/benchmark.json. This is an implementation latency fixture, not a research quality evaluation, network latency estimate or SOTA claim. Local provider cost is zero; live discovery costs depend on the operator's account.

CI produces a synthetic JSON report, verification receipt, escaped HTML report, benchmark and package tarball with SHA256 checksums on each PR and main push. Release tags produce the same tested artifacts. It does not publish npm/PyPI packages, deploy cloud services, or claim that credentials and infrastructure are provisioned.

Acceptance: `node src/cli.mjs generate < fixtures/evidence.json` returns one citation to the relevant fixture, `verify` accepts it, and altering the quote makes verification exit 2. `npm test` must pass including both MCP capability denial and enabled real validation.

## Verification optimization comparison

`node bench/compare.mjs` compares full verification against merged baseline `4702b5124aa3740e2d868f62dad86caef6fd00b8`. It requires a full Git checkout containing that commit, uses only synthetic data, creates a private temporary baseline module and deletes it on completion. No network is used. CI fetches history and stores fresh results as an artifact.

Seven repetitions, each with 50 alternating baseline/candidate iterations after 30 warmup pairs, produced these median of repetition p95 timings on Node 24.19.0 Linux x64:

| Workload | Baseline p95 | Candidate p95 | Reduction |
|---|---:|---:|---:|
| One 100 source report | 2.788 ms | 2.270 ms | 18.6% |
| Ten independent 100 source reports | 24.469 ms | 18.427 ms | 24.7% |

Full raw measurements are in [verification-comparison.json](evidence/verification-comparison.json). Forty varied fixture cases produced equivalent complete reports and citation results. Inputs remained unchanged. These figures measure local verification only, not model quality, live provider latency or deployment throughput. See [ADR 002](adr/002-verification-work.md) for preserved trust boundaries and research context.
