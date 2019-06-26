from urllib import request
import re
import pymysql
import random
import time

class MaoyanSpider(object):
    def __init__(self):
        self.header_list = [{
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'},
            {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'},
            {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'}]
        self.header = random.choice(self.header_list)

        #用来计数
        self.page = 1

        #连接对象
        self.db = pymysql.connect('localhost','root','','maoyandb',charset='utf8')

        self.cursor = self.db.cursor()


    #获取页面
    def get_page(self,url):
        req = request.Request(url,headers=self.header)
        res = request.urlopen(req)
        html = res.read().decode('utf-8')
        self.parse_page(html)
    #解析页面
    def parse_page(self,html):
        p = re.compile('<div class="movie-item-info">.*?title="(.*?)".*?class="star">(.*?)</p>.*?class="releasetime">(.*?)</p>',re.S)
        r_list = p.findall(html)
        self.write_mysql(r_list)

    #保存数据
    def write_mysql(self,r_list):
        ins = 'insert into top(name,star,time) values (%s,%s,%s)'
        for r_t in r_list:
            L = [
                r_t[0].strip(),
                r_t[1].strip(),
                r_t[2].strip()
            ]
            #插入数据库
            self.cursor.execute(ins,L)
            self.db.commit()
    #主程序
    def work_on(self):
        for pn in range(0,91,10):
            url = 'https://maoyan.com/board/4?offset=%s'%str(pn)
            self.get_page(url)
            print('第%d页爬取成功'%self.page)
            self.page+=1
            time.sleep(2)
        #关闭数据库
        self.cursor.close()
        self.db.close()

if __name__ == '__main__':
    begin = time.time()
    spider = MaoyanSpider()
    spider.work_on()
    end = time.time()
    print('执行时间:%.2f'%(end-begin))