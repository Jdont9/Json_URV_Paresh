import json, urllib.request

url = "https://gitlab.com/api/v4/projects/Paresh-Maheshwari%2Fparesh-patches/releases?per_page=1"

with urllib.request.urlopen(url) as r:
    releases = json.loads(r.read())

latest = releases[0]

download_url = None
for asset in latest.get("assets", {}).get("links", []):
    if asset["url"].endswith(".mpp"):
        download_url = asset["url"]
        break

if not download_url:
    raise Exception(f"Aucun fichier .mpp trouvé dans la release {latest['tag_name']}")

created_at = latest["released_at"].split(".")[0].replace("Z", "")

bundle = {
    "version": latest["tag_name"],
    "created_at": created_at,
    "description": latest.get("description", ""),
    "download_url": download_url
}

with open("bundle.json", "w") as f:
    json.dump(bundle, f, indent=2)

print(f"✅ {bundle['version']} — {download_url}")
