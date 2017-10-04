import urllib.request,re
#获取指定网页内的链接,保存到列表list中
#url=input("please input an url: ")
url=r'http://www.njau.edu.cn'
print("list all ip-address in the page")
print("begin:")
try:
	response=urllib.request.urlopen(url,timeout=2)
except:
	print("ERROR !")
else:
    #page=response.read()
    page=response.read().decode("UTF-8")
    #正则表达式筛选网址
    linkre = re.compile('href=\"http.[^\"]*\"')
    list=[url]
    for x in linkre.findall(page):
        if x[6:-1] not in list:
            list.append(x[6:-1])
    i=0
    for x in list:
        print(i," : ",x)
        i+=1
print("end")