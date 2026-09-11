# Reproducible validation

Run on Node 24 with `npm ci --ignore-scripts`, `npm test`, `npm audit --audit-level=moderate` and `npm run benchmark`.

The suite exercises real CLI processes and official SDK MCP subprocesses, source tampering, stale/future times, duplicates, metadata validation, input and response budgets, report comparison, request isolation, HTML escaping, retired Python launchers, provider capability denial, domain enforcement and stalled body cancellation. Provider tests use controlled response fixtures. There was no paid provider request.

The benchmark warms ten iterations, then builds and queries 100 synthetic sources 100 times. It measures the complete local report construction including snapshots, BM25 selection and canonical hashing. Exact results are in evidence/benchmark.json. This is an implementation latency fixture, not a research quality evaluation, network latency estimate or SOTA claim. Local provider cost is zero; live discovery costs depend on the operator's account.

CI produces a synthetic JSON report, verification receipt, escaped HTML report, benchmark and package tarball with SHA256 checksums on each PR and main push. Release tags produce the same tested artifacts. It does not publish npm/PyPI packages, deploy cloud services, or claim that credentials and infrastructure are provisioned.

Acceptance: `node src/cli.mjs generate < fixtures/evidence.json` returns one citation to the relevant fixture, `verify` accepts it, and altering the quote makes verification exit 2. `npm test` must pass including both MCP capability denial and enabled real validation.
