#!/usr/bin/env python3
"""Inject PWA head tags + service-worker registration into every HTML page.

Idempotent: skips files that already carry the manifest <link>.
Computes each file's relative path to the repo root so the href/src attributes
resolve correctly regardless of how deeply the file is nested.
"""
from pathlib import Path
import re
import sys

REPO = Path(__file__).parent.parent
SENTINEL = 'rel="manifest"'

# List every HTML file in the course.
def html_files():
    for p in REPO.rglob("*.html"):
        if ".git" in p.parts:
            continue
        yield p

def rel_prefix(file_path: Path) -> str:
    """Return the relative prefix from a file back to the repo root."""
    depth = len(file_path.relative_to(REPO).parts) - 1
    return "./" if depth == 0 else "../" * depth

HEAD_BLOCK_TEMPLATE = """
  <link rel="manifest" href="{p}manifest.webmanifest">
  <meta name="theme-color" content="#4e38d9" media="(prefers-color-scheme: light)">
  <meta name="theme-color" content="#0a0a12" media="(prefers-color-scheme: dark)">
  <meta name="application-name" content="ultimate·css">
  <meta name="apple-mobile-web-app-title" content="ultimate·css">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <meta name="mobile-web-app-capable" content="yes">
  <link rel="apple-touch-icon" href="{p}assets/icons/apple-touch-icon.png">
  <link rel="icon" type="image/svg+xml" href="{p}assets/icons/icon.svg">
  <link rel="icon" type="image/png" sizes="32x32" href="{p}assets/icons/favicon-32.png">
  <link rel="icon" type="image/png" sizes="192x192" href="{p}assets/icons/icon-192.png">"""

BODY_SCRIPT_TEMPLATE = '  <script src="{p}assets/js/pwa.js" defer></script>\n'


def inject(file_path: Path) -> bool:
    text = file_path.read_text(encoding="utf-8")
    if SENTINEL in text:
        return False  # already injected

    prefix = rel_prefix(file_path)
    head_block = HEAD_BLOCK_TEMPLATE.format(p=prefix)
    body_script = BODY_SCRIPT_TEMPLATE.format(p=prefix)

    # Insert the head block immediately after the existing <link rel="stylesheet" ... main.css">.
    head_re = re.compile(r'(<link\s+rel="stylesheet"\s+href="[^"]*main\.css">)')
    m = head_re.search(text)
    if not m:
        print(f"SKIP (no main.css link): {file_path.relative_to(REPO)}", file=sys.stderr)
        return False
    text = text[:m.end()] + head_block + text[m.end():]

    # Insert the pwa.js script immediately before </body>.
    body_re = re.compile(r'(\s*)</body>')
    m2 = body_re.search(text)
    if not m2:
        print(f"SKIP (no </body>): {file_path.relative_to(REPO)}", file=sys.stderr)
        return False
    text = text[:m2.start()] + "\n" + body_script + m2.group(0).lstrip("\n") + text[m2.end():]

    file_path.write_text(text, encoding="utf-8")
    return True


def main():
    written = 0
    skipped = 0
    for f in html_files():
        if inject(f):
            written += 1
        else:
            skipped += 1
    print(f"updated {written} file(s), skipped {skipped}")


if __name__ == "__main__":
    main()
