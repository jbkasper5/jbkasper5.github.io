#!/usr/bin/env python3
"""Embed boot.log into index.html.

Why: when the page is opened directly (double-clicked -> file://), browsers block
fetch() of local files, so the live boot.log can't be read. This copies the current
boot.log into an inert <script id="bootlog"> block that the page uses as a fallback.

You only need this for the double-click workflow. When the site is hosted or served
over http:// (e.g. `python3 -m http.server`), boot.log is read live and this snapshot
is ignored.

Usage:  python3 sync-log.py
"""
import re
import sys
import pathlib

here = pathlib.Path(__file__).resolve().parent
log_path = here / "boot.log"
html_path = here / "index.html"

if not log_path.exists():
    sys.exit("boot.log not found next to this script")

log = log_path.read_text(encoding="utf-8", errors="replace")
# make sure the log text can never close the <script> block early
log = re.sub(r"</(?=script)", r"<\\/", log, flags=re.I).rstrip("\n")

html = html_path.read_text(encoding="utf-8")
pattern = re.compile(
    r'(<script type="text/plain" id="bootlog">)(.*?)(</script>)', re.S
)
if not pattern.search(html):
    sys.exit('could not find the <script id="bootlog"> block in the HTML')

html = pattern.sub(lambda m: m.group(1) + "\n" + log + "\n" + m.group(3), html)
html_path.write_text(html, encoding="utf-8")
print(f"Embedded {log.count(chr(10)) + 1} log lines into {html_path.name}")
