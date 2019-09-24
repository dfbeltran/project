import requests

# URL
url = 'http://localhost:1080/linear_reg'

# Change the value of experience that you want to test
r = requests.post(url, json={'exp': 0})
print(r.json())