##请输入你想要搜索的内容:
## 保存到本地文件:...html
import urllib.request
import urllib.parse

##首先拼接一个url
baseurl = 'http://www.baidu.com/s?'
key = input('请输入你要搜索的内容:')
#进行urlencode()编码转换
d = {'wd':key}
key = urllib.parse.urlencode(d)

url1 = baseurl+key

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

res = urllib.request.Request(url1,headers=header)
#获取响应对象
with urllib.request.urlopen(res) as response:
#响应对象read().decode('utf-8')
    page = response.read().decode('utf-8')
with open('aa.html','w',encoding='utf-8')as f:
    f.write(page)
    f.close()