import requests
import random
url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1561542011797&di=1a66a611aa98277a91ba2fc3e20512d9&imgtype=jpg&src=http%3A%2F%2Fimg3.imgtn.bdimg.com%2Fit%2Fu%3D160734923%2C2844137609%26fm%3D214%26gp%3D0.jpg'
headers_list = [{
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'},
            {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'},
            {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'}]
headers = random.choice(headers_list)

res = requests.get(url,headers=headers)
res.encoding = 'utf-8'

#获取bytes数
html = res.content

#写文件
with open('panda.jpg','wb') as f:
    f.write(html)