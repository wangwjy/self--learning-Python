import urllib.request,json
url=r'https://api.github.com/'
print("begin:")
response=urllib.request.urlopen(url)
page=response.read()
page=page.decode('UTF-8')
page=eval(page)
for i in page:
    if r"https://" or R"http://" in page[i]:
        print(page[i])
print("end")