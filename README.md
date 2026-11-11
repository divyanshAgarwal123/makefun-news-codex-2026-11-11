# make.fun: news-summary-01

A fixed English digest of world news that happened or was first reported on
Wednesday 11 November 2026. Twelve items, ranked by consequence, cover diplomacy,
conflict, public health, climate, nuclear authority, labor, politics, the economy,
technology, markets and school security. The two Ebola reports share one item.
Claims, allegations and denials remain attributed; Kenya's last patient discharge
is distinguished from a possible Ebola-free declaration.

This revision uses the user's verified source notes and this entry's existing
supplied sources, with original wording. No network requests were made, no source
pages were fetched, and no other entrant's text was consulted.

## Run

Requires Python 3.13; no dependencies or installation steps.

```sh
python3.13 main.py
```

By default this writes `/output/entry.txt`. For a local run:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/makefun-news-local python3.13 main.py
```

`main.py` reads `summary.txt` relative to its own location, strictly decodes
UTF-8, validates the inclusive 1–2,000 Unicode character limit, rejects
whitespace-only summaries, and writes the original bytes without trimming.
The summary has 1,800 Unicode characters, including its final newline.
There are no timestamps, random values or runtime news lookups.

## Reproduce the checks

Run from the repository root. Temporary outputs stay outside the repository.

```sh
python3.13 - <<'PY'
import os
from pathlib import Path
import subprocess
import sys
import tempfile

assert sys.version_info[:2] == (3, 13)
source = Path('summary.txt').read_bytes()
with tempfile.TemporaryDirectory() as temp:
    outputs = []
    for run in ('first', 'second'):
        target = Path(temp) / run
        env = dict(os.environ, MAKEFUN_OUTPUT_DIR=str(target))
        subprocess.run([sys.executable, 'main.py'], env=env, check=True)
        outputs.append((target / 'entry.txt').read_bytes())
    assert outputs[0] == outputs[1] == source
    count = len(source.decode('utf-8'))
    assert 1 <= count <= 2000
    assert source.decode('utf-8').strip()
    print(f'PASS: identical outputs; {count} Unicode characters')
PY
```

## Sources

Each item names its outlet in the summary. These are the supplied links for
11 November reporting, in summary order:

1. [AP: Russia-Ukraine talks](https://apnews.com/article/7c8d1024302e0c6ad8be064eec852a64)
2. [Al Jazeera/Reuters: Iran and Hormuz](https://www.aljazeera.com/news/2026/11/11/iran-denies-talks-with-us-says-hormuz-will-stay-shut-until-demands-are-met)
3. [AP: Gaza shelter supplies](https://apnews.com/article/50075bc97e07d41fa3b66fc28858c06b)
4. [AP: DR Congo Ebola outbreak](https://apnews.com/article/cae4cef6e48c1d2210a59c72676bff29) and [AP: Kenya's last Ebola patient discharged](https://apnews.com/article/74689c9faa169dafeee5d21852fde992)
5. [AP: COP31 talks](https://apnews.com/article/056ff011b2e6f324c2cd089862c13824) and [AP: zero waste and island vulnerability](https://apnews.com/article/a72471f4211e539980bfe6f0a5dc6005)
6. [NK News: revised North Korean constitution](https://www.nknews.org/2026/11/north-korea-posts-text-of-revised-constitution-confirming-kims-expanded-powers/)
7. [AP: Spain's general strike](https://apnews.com/article/68a061a72d7cdf842b7803a816e46ef0)
8. [AP: White House warning to investigators](https://apnews.com/article/12acd4e233792f687b80eb9636aea18d)
9. [AP: China's Singles' Day spending](https://apnews.com/article/3076aecc8a3cda0963217bccd43db4dd)
10. [AP: bipartisan calls to investigate allegations involving Nvidia's CEO](https://apnews.com/article/56e1c03b4797c38aa04f4804f7cdf4db)
11. [AP: AI stocks rebound; Nvidia gains 2.9%](https://apnews.com/article/297d040c83844a9563327340b370c24e)
12. [AP: Italian school bomb threats](https://apnews.com/article/0f312fda4ee2e9cdcebd0d6e1a40d9e8)

License: MIT. Copyright Divyansh Agarwal 2026.
