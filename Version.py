import requests
url = "https://api.github.com/repos/sourabhkv/ytdl/releases/latest"
r = requests.get(url)
if r.status_code==200:
    latest_ver = r.json()["tag_name"]
    intver = int(latest_ver[1:].replace(".",""))
    print(latest_ver, intver)