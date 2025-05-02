"""
goes into coin api and gets price of 1 bitcoin.
user can put how many bitcoins and it will convert to usd
"""


import sys
import requests
import json


if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit()
try:
    bitcoins = float(sys.argv[1])
except ValueError:
    print("Command-line argument is not a number")
    sys.exit()
    
try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=c296b09bd5169216d74b3c95ff83f7e708713472b44bf4c96c20696966e5cf1f")
    price = float(response.json()["data"]["priceUsd"])
    output = price * bitcoins
    print(f"${output:,.4f}")
    
except requests.RequestException:
    sys.exit()
