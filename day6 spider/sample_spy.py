import urllib.request

path='http://www.baidu.com'

reponse=urllib.request.urlopen(path)
html=reponse.read().decode('utf-8')
print(type(html))
print(html)

#encode  字符串 --> bytes数据类型
#decode  bytes数据类型 -->字符串