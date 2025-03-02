import requests

json_put = [
    {
        "name": "morpheus",
        "job": "zion resident"
    }
]
print(requests.post(url="https://reqres.in/api/users/3", json=json_put).json())
# print(requests.post(url="https://reqres.in/api/login", json=json_post).json())