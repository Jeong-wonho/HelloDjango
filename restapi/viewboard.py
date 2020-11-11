import requests
url = 'http://127.0.0.1:8000/rest/boards/6'

res = requests.get(url)

res.encoding = 'utf-8'
print(res)
print(res.text)
