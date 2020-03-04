import requests

url = ""
data = {}

headers = {"Content-Type": "application/json;charset=UTF-8"}
res = requests.request("post", url, json=data, headers=headers)

print(res.status_code)
print(res.text)
