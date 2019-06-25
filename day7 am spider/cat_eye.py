import csv
import re
from urllib import request,parse
import time
import random

class CatEye(object):
    def __init__(self):
        self.page = 1
        self.header_list = [{
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'},
            {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'},
            {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'}]
        self.header = random.choice(self.header_list)
    #获取页面
    def get_page(self,url):
        req = request.Request(url,headers=self.header)
        res = request.urlopen(req)
        html = res.read().decode('utf-8')
        #直接调用解析函数,去对html做解析
        self.parse_page(html)
    def parse_page(self,html):
        p = re.compile('<div class="movie-item-info">.*?title="(.*?)".*?class="star">(.*?)</p>.*?class="releasetime">(.*?)</p>',re.S)
        r_list = p.findall(html)
        #r_list = ['霸王别姬','张国荣','1993-1-1',(),()]
        #直接调用保存数据
        self.write_csv(r_list)
    #保存数据函数
    def write_csv(self,r_list):
        with open('cat_eye.csv','a')as f:
            #初始化对象
            writer = csv.writer(f)
            #依次写入每个电影信息
            for r_t in r_list:
                film = [
                    r_t[0].strip(),
                    r_t[1].strip(),
                    r_t[2].strip()
                ]
                writer.writerow(film)
    #主方法
    def work_on(self):
        for pn in range(0,41,10):
            url = 'https://maoyan.com/board/4?offset=%s'%str(pn)
            self.get_page(url)
            print('第%d页爬取成功'%self.page)
            self.page+=1
            time.sleep(2)

if __name__ == '__main__':
    begin = time.time()
    spider = CatEye()
    spider.work_on()
    end = time.time()
    print('执行时间:%.2f'%(end-begin))