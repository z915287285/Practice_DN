import re

html='''
<div class = "animal">
		  <p class = "name">
			<a title = "Tiger"></a>
		  </p>
		  
		  <p class = "contents">
			Two tigers two tigers run fast
		  </p>
</div>
<div class = "animal">
		  <p class = "name">
			<a title = "rabbit"></a>
		  </p>
		  
		  <p class = "contents">
			small white rabbit white white
		  </p>
</div>'''

p = re.compile('<div class = "animal">.*?title = (.*?)>.*?class = "contents">(.*?)</p>',re.S)
list = p.findall(html)
print(list)

for i in list:
    print("动物名称：%s"%i[0])
    print("动物描述：%s" % i[1])