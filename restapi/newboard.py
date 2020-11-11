import requests

url = 'http://127.0.0.1:8000/rest/boards/create/'

data = {'title':'이글이보이나요?', 'contents':'새글새글', 'userid':'새글새글~'}

res = requests.post(url, data=data)

print(res)
print(res.text)