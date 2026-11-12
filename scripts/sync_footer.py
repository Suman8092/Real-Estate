"""Copy the homepage footer to the site's standalone HTML pages."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOOTER = re.compile(r'<footer\b[^>]*>.*?</footer>', re.DOTALL)
LOCAL_URL = re.compile(r'((?:href|src)=")(?![a-z]+:|[#/])')


def shared_footer(prefix):
    homepage = (ROOT / 'index.html').read_text(encoding='utf-8')
    footer = FOOTER.search(homepage).group()
    return LOCAL_URL.sub(lambda match: match[1] + prefix, footer)


def sync_footer(html, prefix):
    html, count = FOOTER.subn(lambda _: shared_footer(prefix), html)
    if count != 1:
        raise ValueError(f'Expected one footer, found {count}')
    stylesheet = f'<link rel="stylesheet" href="{prefix}css/shared-footer.css" />'
    if stylesheet not in html:
        html = html.replace('</head>', f'  {stylesheet}\n</head>', 1)
    return html


if __name__ == '__main__':
    for path in sorted([*ROOT.glob('*.html'), *(ROOT / 'properties').glob('*.html')]):
        if path.name == 'index.html':
            continue
        prefix = '../' if path.parent != ROOT else ''
        html = path.read_bytes().decode('utf-8')
        path.write_bytes(sync_footer(html, prefix).encode('utf-8'))
