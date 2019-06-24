##请输入你想要搜索的内容:
## 保存到本地文件:...html
import urllib.request
import urllib.parse
import time
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
##主程序
##首先拼接一个url
baseurl = 'http://tieba.baidu.com/f?'
key = input('请输入你要抓取的贴吧:')
begin = int(input('请输入起始页:'))
end = int(input('请输入终止页:'))

#进行urlencode()编码转换
d = {'kw':key}
key = urllib.parse.urlencode(d)
for i in range(begin,end+1):
    pn='&pn='+str(i-1 if i!=0 else 0)
    url1 = baseurl+key+pn
    ##请求对象
    res = urllib.request.Request(url1,headers=header)
    #获取响应对象
    with urllib.request.urlopen(res) as response:
    #响应对象read().decode('utf-8')
        time.sleep(2)
        page = response.read().decode('utf-8')
    with open('./tieba/'+str(i)+'.html','w',encoding='utf-8')as f:
        print('正在爬取第%d页'%i)
        f.write(page)
        f.close()
        print('爬取成功第%d页'%i)