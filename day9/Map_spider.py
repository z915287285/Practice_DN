import requests
from bs4 import BeautifulSoup
import csv
import random
from time import sleep

User_Agent = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
              'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
              'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)',
              'Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50']
headers = {'User-Agent':User_Agent[random.randint(0,4)],
           'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8',
'Accept - Encoding': 'gzip, deflate, br',
'Accept - Language':' zh - CN, zh;q = 0.9',
'Cache - Control': 'max - age = 0',
'Connection': 'keep - alive'
}

csvfile = open('去哪儿网景点.csv','w',enconding ='utf-8',newline='')
writer = csv.writer(csvfile)
writer.writerow(['自然风光','文化古迹','公园','农家度假','游乐场','展馆','山川','古建筑','城市观光','运动健身'])
#发送请求并获取响应
def download_page(url):
    try:
        data = requests.get(url,headers=headers,allow_redirects=True).content
        return data
    except:
        pass

#请求失败后，等待1秒再请求
def download_page_sleep_01(url):
    try:
        res = requests.get(url,headers=headers,allow_redirects=False,timeout=5)
        #如果请求成功
        if res.status_code ==200:
            html = res.content
            html = html.decode('utf-8')
            soup = BeautifulSoup(html,'html.parser')
            return soup
        else:
            sleep(1)
            print('稍安务躁，等待1s')
            return download_page_sleep_01(url)
    except:
        return ""