import requests

json_post = [
    {
        "email": "peter@klaven"
    }
]
print(len(requests.get(url="https://reqres.in/api/unknown/2").json()['data']))
# print(requests.post(url="https://reqres.in/api/login", json=json_post).json())