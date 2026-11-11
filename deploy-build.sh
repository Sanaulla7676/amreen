#!/bin/sh
set -eu
python3 -c "import gzip,pathlib; p=pathlib.Path('.deploy'); pathlib.Path('build.py').write_bytes(gzip.decompress((p/'build.py.gz').read_bytes())); a=pathlib.Path('assets'); a.mkdir(exist_ok=True); (a/'style.css').write_bytes(gzip.decompress((p/'style.css.gz').read_bytes())); (a/'main.js').write_bytes(gzip.decompress((p/'main.js.gz').read_bytes()))"
mkdir -p public/assets
cp assets/style.css assets/main.js public/assets/
(cd public && python3 ../build.py)
