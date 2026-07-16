import urllib.request
import re
try:
    html = urllib.request.urlopen("https://skillicons.dev").read().decode("utf-8")
    icons = set(re.findall(r'title="([^"]+)"', html))
    print(icons)
except Exception as e:
    print(e)
