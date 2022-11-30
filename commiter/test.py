import requests

data = {"id1": 1}
a = requests.get("http://127.0.0.1:9000/get_user", json=data)
print(a.text)
