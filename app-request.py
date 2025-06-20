import requests

response = requests.get("http://35.206.76.195:8062/head?count=10")


#check if request worked

print(response.status_code)
print(response.headers)

data = response.json()
print(type(data))
print(data)

