"""
Remove all html-minifier references from remaining files.
"""
import os, re

base = r'L:\垃圾项目\dev-toolkit'

# 1. index.original.html
fp = os.path.join(base, 'index.original.html')
with open(fp, 'r', encoding='utf-8') as f:
    c = f.read()
c, n = re.subn(r"\{name:'HTML Minifier',desc:'[^']*',url:'tools/code/html-minifier\.html',cat:'code',icon:'[^']*'\},\n?", '', c)
if n:
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f'index.original.html: removed {n}')

# 2. sitemap.xml
fp = os.path.join(base, 'sitemap.xml')
with open(fp, 'r', encoding='utf-8') as f:
    c = f.read()
c, n = re.subn(r'<url><loc>https://yurukusa\.github\.io/html-minifier/</loc>.*?</url>\n?', '', c, flags=re.DOTALL)
if n:
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f'sitemap.xml: removed {n}')

# 3. tests/run.mjs
fp = os.path.join(base, 'tests', 'run.mjs')
with open(fp, 'r', encoding='utf-8') as f:
    c = f.read()
c, n = re.subn(r"  'html-minifier': \{ skipAll: true \},\n?", '', c)
if n:
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f'tests/run.mjs: removed {n}')

# 4. Tool files with links to html-minifier
tool_files = [
    'tools/design/svg-optimizer.html',
    'tools/code/css-minifier.html',
    'tools/code/html-escape.html',
    'tools/code/html-to-jsx.html',
    'tools/code/js-minifier.html',
    'tools/code/js-beautifier.html',
    'tools/design/css-reset.html',
]

for rel_fp in tool_files:
    fp = os.path.join(base, rel_fp)
    with open(fp, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # Remove html-minifier link references (various patterns)
    new_c, n = re.subn(
        r' \| <a href="https://gokuscraper\.github\.io/dev-vault/html-minifier/?"[^>]*>HTML Minifier</a>',
        '', c
    )
    if n == 0:
        # Try alternative pattern with ti attribute
        new_c, n = re.subn(
            r' \| <a href="https://gokuscraper\.github\.io/dev-vault/html-minifier/"[^>]*>HTML Minifier</a>',
            '', c
        )
    if n == 0:
        # Try yet another pattern
        new_c, n = re.subn(
            r'<a href="https://gokuscraper\.github\.io/dev-vault/html-minifier/"[^>]*>HTML Minifier</a>',
            '', c
        )
    
    if n > 0:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(new_c)
        print(f'{rel_fp}: removed {n} link(s)')
    else:
        print(f'{rel_fp}: NOT FOUND')
