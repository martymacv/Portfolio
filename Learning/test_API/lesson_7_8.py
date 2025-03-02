import json

import requests

json_put = [
    {
        "name": "morpheus",
        "job": "zion resident"
    }
]
fields = json.loads(requests.get(url="https://catfact.ninja/facts?max_length=100&limit=5").text)
print(list(fields))
