import requests
import sys
import json

try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        float(sys.argv[1])
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=88c2afe2bd34d2102c32254cc48bd2134c9aa3ea8884ef7557fd2a1586028c4f")
        x = response.json()
        for data in x:
            value = float(sys.argv[1]) * float(x["data"]["priceUsd"])
        print(f"${value:,.4f}")

    except(ValueError):
        sys.exit("Command-line argument is not a number")

except requests.RequestException:
    sys.exit("error")
