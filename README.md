# jakekasper.com

Personal website of Jake Kasper — software / systems engineer.

A static site (plain HTML/CSS/JS, no build step). The homepage background streams a
live boot-log trace from my bare-metal OS project,
[rpos](https://github.com/jbkasper5/rpos).

## Built with AI assistance

I built this site with the help of AI tools — specifically Anthropic's **Claude**
(via Claude Code). Claude did most of the design and front-end implementation
(layout, styling, the scrolling log-trace effect); the direction, content, project
write-ups, and the `boot.log` data are mine.

I'm noting this on purpose: AI is part of how I work, and I'd rather be upfront that
this site was AI-assisted than imply I hand-wrote every line.

## Local preview

Serve over HTTP so the background reads from `boot.log`:

```sh
python3 -m http.server 8000
# then open http://localhost:8000
```

Opening `index.html` directly also works — it falls back to an embedded copy of the
log when the browser blocks local file reads.

## Updating the boot log

Replace `boot.log` with a newer trace. When the site is served/hosted it's read live.
For the double-click (file://) case, refresh the embedded fallback with:

```sh
python3 sync-log.py
```

## Deploy

Served via GitHub Pages on the `jakekasper.com` custom domain (see `CNAME`).
