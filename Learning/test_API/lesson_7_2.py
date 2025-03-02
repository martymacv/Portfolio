import requests

json_post = [
    {
        "email": "peter@klaven"
    }
]
print(requests.post(url="https://reqres.in/api/login", json=json_post).status_code)
print(requests.post(url="https://reqres.in/api/login", json=json_post).json())
# print(len(requests.post(url="https://petstore.swagger.io/v2/user/createWithArray", json=json_post).json()['token']))
