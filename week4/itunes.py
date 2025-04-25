import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit("has to be 1 argument")

lol = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])


o = lol.json()
for result in o["results"]:
    print(result["trackName"])
