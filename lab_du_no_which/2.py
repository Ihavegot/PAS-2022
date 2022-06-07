import requests

res = requests.get("http://httpbin.org/image/png")

file = open('image.png', 'wb')
file.write(res.content)
file.close()
