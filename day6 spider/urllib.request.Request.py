import urllib.request

url='http://www.baidu.com/'
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
#创建请求对象
res=urllib.request.Request(url,headers=header)
#获取响应对象
with urllib.request.urlopen(res) as response:
#响应对象read().decode('utf-8')
    page = response.read().decode('utf-8')
print(page)