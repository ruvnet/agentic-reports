"""Retired legacy launcher. No credentials, installs, or network calls."""
import sys
def main():
    sys.stderr.write("Legacy Python API retired. Use Node 24: npm ci && node src/cli.mjs status. See README.md.\n")
    return 2
if __name__ == "__main__":
    raise SystemExit(main())
