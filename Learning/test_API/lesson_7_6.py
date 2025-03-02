import requests

json_put = [
    {
        "name": "morpheus",
        "job": "zion resident"
    }
]
print(requests.delete(url="https://reqres.in/api/users/2").status_code)
