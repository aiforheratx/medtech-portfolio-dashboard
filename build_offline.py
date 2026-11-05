"""Build dashboard-offline.html: one self-contained file (no internet needed).
Run:  python3 build_offline.py"""
import json, pathlib
root = pathlib.Path(__file__).parent
html = (root / 'index.html').read_text()
lib = (root / 'vendor/echarts.min.js').read_text().replace('</script', '<\\/script')
world = json.dumps(json.loads((root / 'vendor/world.json').read_text()), separators=(',', ':'))
start = html.index('<script src="vendor/echarts.min.js"></script>')
end = html.index('</script>', html.index('<script>window.echarts ||')) + len('</script>')
html = html[:start] + '<script>' + lib + '</script>\n<script>window.WORLD_JSON=' + world + ';</script>' + html[end:]
(root / 'dashboard-offline.html').write_text(html)
print('wrote dashboard-offline.html', round(len(html) / 1e6, 2), 'MB')
