import requests

url = "https://httpbin.org/post"
data = dict(title="Sesion python 22", author="Ricardo")

response = requests.post(url, data=data)
print("Response:")
print(response.json())

d = {
    'statemenmt': 'select * from users;'
}

