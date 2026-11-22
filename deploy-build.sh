#!/bin/sh
set -eu
ROOT="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
cd "$ROOT"
rm -rf public
mkdir -p public/assets
for page in index.html about.html courses.html professional-makeup.html skin-aesthetics.html hair-styling.html bridal-artistry.html 45-day-course.html faculty.html student-success.html blog.html faqs.html contact.html crm.html; do
  cp "$page" public/
done
node - <<'NODE'
const fs = require('node:fs');
const config = {
  url: process.env.NEXT_PUBLIC_SUPABASE_URL || '',
  publishableKey: process.env.NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY || '',
};
fs.writeFileSync('js/crm-config.js', `window.ACADEMY_SUPABASE_CONFIG = ${JSON.stringify(config)};\n`);
NODE
cp -R css public/
cp -R js public/
cp -R assets/. public/assets/
find public/assets -type f \( -name '*.mp4' -o -name '*.b64' \) -delete
