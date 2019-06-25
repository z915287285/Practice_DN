#函数版
import urllib.parse
import urllib.request
import random
import time
#获取请求对象
def getRequest(url):
    #自定义 headers
    header_list = [{'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'},
    {'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'},
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'}]
    headers = random.choice(header_list)
    rep = urllib.request.Request(url,headers=headers)

    return rep
#获取响应对象
def getResponse(rep):
    response = urllib.request.urlopen(rep)
    time.sleep(2)
    html = response.read().decode('utf-8')
    return html

#保存页面
def saveFile(page,i):
    with open('./tieba/' + str(i) + '.html', 'w', encoding='utf-8')as f:
        print('正在爬取第%d页' % i)
        f.write(page)
        f.close()
        print('爬取成功第%d页' % i)

def main():
    ##主程序
    ##首先拼接一个url
    baseurl = 'http://tieba.baidu.com/f?'
    key = input('请输入你要抓取的贴吧:')
    begin = int(input('请输入起始页:'))
    end = int(input('请输入终止页:'))

    # 进行urlencode()编码转换
    d = {'kw': key}
    key = urllib.parse.urlencode(d)
    ##拼接URL，发送请求，获取响应
    for i in range(begin,end+1):
        pn = '&pn=' + str(i - 1 if i != 0 else 0)
        url1 = baseurl + key + pn
        res = getRequest(url1)
        page = getResponse(res)
        #写入文件
        saveFile(page,i)
if __name__ == '__main__':
    main()
