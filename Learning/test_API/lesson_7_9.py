import json

import requests

json_put = [
    {
        "name": "morpheus",
        "job": "zion resident"
    }
]
fields = requests.get(url="https://dog.ceo/api/breed/hound/images").json()
print(fields['message'])
print(len(list(filter(lambda x: 'hound-english' in x, fields['message']))))
#hound-english