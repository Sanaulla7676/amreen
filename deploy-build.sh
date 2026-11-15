#!/bin/sh
set -eu
ROOT="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
cd "$ROOT"
rm -rf public
mkdir -p public/assets
for page in index.html about.html courses.html professional-makeup.html skin-aesthetics.html hair-styling.html bridal-artistry.html 45-day-course.html faculty.html student-success.html blog.html faqs.html contact.html; do
  cp "$page" public/
done
cp -R css public/
cp -R js public/
cp -R assets/. public/assets/
find public/assets -type f \( -name '*.mp4' -o -name '*.b64' \) -delete