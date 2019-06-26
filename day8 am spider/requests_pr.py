import requests
import random
url = 'https://www.baidu.com/'
headers_list = [{
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'},
            {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'},
            {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'}]
headers = random.choice(headers_list)

res = requests.get(url,headers=headers)
res.encoding = 'utf-8'
html = res.text

#查看字符编码
print(res.encoding)

#获取bytes数据类型
print(type(res.content))

#响应码
print(res.status_code)