import urllib.request

res = urllib.request.urlopen("http://httpbin.org/html")
html_res = res.read().decode("utf8")
res.close()

file = open('index.html', 'w')
file.write(html_res)
file.close()