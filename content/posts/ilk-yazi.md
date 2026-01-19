+++
date = '2026-01-19T23:14:48+03:00'
draft = false
title = 'Test Article for Medium Import'
+++

This is a short, mixed-format article meant to test Medium import from HTML.

## What this post includes

- Headings and subheadings
- A short bullet list
- A numbered list
- A blockquote
- Inline code and a code block
- A simple table

## Quick narrative

I set up this Hugo site to publish only posts from `content/posts/`.
The goal is to export clean HTML and import it into Medium without surprises.
This page exercises the most common Markdown features Medium accepts.

> If the import works well, the structure and formatting should match what you see here.

## Steps I plan to follow

1. Write posts in Markdown.
2. Generate HTML with Hugo.
3. Import the HTML into Medium.
4. Review formatting and fix any discrepancies.

## Code sample

Here is a tiny snippet just to verify formatting:

```text
curl -X POST https://example.com/import \
  -H "Content-Type: text/html" \
  --data-binary "@public/posts/ilk-yazi/index.html"
```

## Small table

| Item | Purpose |
| --- | --- |
| Title | Headline check |
| Quote | Typography check |
| Code | Monospace check |

## Final note

If everything looks correct in Medium, I will keep this post as a template for future articles.
