import urllib.request
import urllib.parse
import random
import time

class Tieba():
    def __init__(self,baseline):
        self.baseline = baseline
        self.header_list = [{
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'},
            {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'},
            {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'}]
    def getRequest(self,pn,key):
        # 自定义 headers
        headers = random.choice(self.header_list)
        rep = urllib.request.Request(self.baseline+key+pn, headers=headers)

        return rep

    # 获取响应对象
    def getResponse(self,rep):
        response = urllib.request.urlopen(rep)
        time.sleep(1)
        html = response.read().decode('utf-8')
        return html
    #读取页面
    def readPage(self,key,pn,i):
        rep = self.getRequest(pn,key)
        html = self.getResponse(rep)
        self.saveFile(html,i)
    # 保存页面
    def saveFile(self,page, i):
        with open('./tieba/' + str(i) + '.html', 'w', encoding='utf-8')as f:
            print('正在爬取第%d页' % i)
            f.write(page)
            f.close()
            print('爬取成功第%d页' % i)

    def work(self):
        key = input('请输入你要抓取的贴吧:')
        begin = int(input('请输入起始页:'))
        end = int(input('请输入终止页:'))

        # 进行urlencode()编码转换
        d = {'kw': key}
        key = urllib.parse.urlencode(d)
        ##拼接URL，发送请求，获取响应
        for i in range(begin, end + 1):
            pn = '&pn=' + str(i - 1 if i != 0 else 0)
            self.readPage(key,pn,i)

if __name__ == '__main__':
    baseurl = 'http://tieba.baidu.com/f?'
    spider = Tieba(baseline=baseurl)
    spider.work()