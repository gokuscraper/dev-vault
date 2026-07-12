"""
Remove EN/zh language toggle from all tool HTML files.
"""
import os, re, sys

tools_dir = sys.argv[1] if len(sys.argv) > 1 else r'L:\垃圾项目\dev-toolkit\tools'

TOGGLE_RE = re.compile(
    r'<div\s+class="lb"\s+style="position:absolute;[^"]*">'
    r'<button\s+class="lb"\s+dl="en"\s+onclick="sL\(\'en\'\)"[^>]*>EN</button>'
    r'<button\s+class="lb"\s+dl="zh"\s+onclick="sL\(\'zh\'\)"[^>]*>\u4e2d</button>'
    r'</div><style>\.lb\.a\{background:[^}]*\}</style>',
    re.I
)

total = 0
modified = 0

for root, dirs, files in os.walk(tools_dir):
    for fn in sorted(files):
        if not fn.endswith('.html'):
            continue
        fp = os.path.join(root, fn)
        with open(fp, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content, n = TOGGLE_RE.subn('', content)
        if n == 0:
            continue

        # Handle duplicates (some files had 2-3 from multiple injections)
        new_content, n2 = TOGGLE_RE.subn('', new_content)
        total_n = n + n2

        with open(fp, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'  [{fn}] removed {total_n} toggle(s)')
        modified += 1
        total += 1

print(f'\nDone: {modified} files modified')
