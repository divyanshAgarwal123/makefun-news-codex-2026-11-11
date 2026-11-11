# make.fun: news-summary-01

A fixed English digest of world news that happened or was first reported on
11 November 2026. Ten items cover diplomacy, conflict, public health, climate,
nuclear authority, labor, politics, the economy and school security. The two
Ebola reports share one item. Claims and denials remain attributed.

The entry uses only the verified facts and links supplied in the competition
brief. No network requests were made, and no source pages were fetched.
All project files were authored in this session without using another repository.

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
UTF-8, validates the inclusive 1–2,000 Unicode character limit, and writes the
original bytes. The summary has 1,722 characters, including its final newline.
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
10. [AP: Italian school bomb threats](https://apnews.com/article/0f312fda4ee2e9cdcebd0d6e1a40d9e8)

License: MIT. Copyright Divyansh Agarwal 2026.
