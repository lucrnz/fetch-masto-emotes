from requests import get as requests_get
from os import path, mkdir, environ

instance = environ["INSTANCE"]
instance_folder = f"./{instance}"

if not path.exists(instance_folder):
    mkdir(instance_folder)

def download_emote(shortcode : str, url : str):
    print(f"Downloading {shortcode}...")
    r = requests_get(url, allow_redirects=True)
    open(f"{instance_folder}/{shortcode}.png", "wb").write(r.content)

response = requests_get(f"https://{instance}/api/v1/custom_emojis")
emotes = response.json()
for emote in emotes:
    download_emote(shortcode=emote["shortcode"], url=emote["url"])
