"""Write the fixed news summary using only the Python standard library."""

import os
from pathlib import Path


def main() -> None:
    payload = Path(__file__).with_name("summary.txt").read_bytes()
    summary = payload.decode("utf-8", errors="strict")
    if not 1 <= len(summary) <= 2000:
        raise ValueError(f"Summary must contain 1–2,000 Unicode characters; got {len(summary)}")
    if not summary.strip():
        raise ValueError("Summary must contain non-whitespace text")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(payload)


if __name__ == "__main__":
    main()
