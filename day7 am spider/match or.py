import re

html = '''
<div><p>王者荣耀,刺激战场，阴阳师</p></div>
<div><p>地下城与勇士,穿越火线</p></div>
'''
##用贪婪模式与非贪婪模式匹配查看结果??
#运行结果['王者荣耀,刺激战场，阴阳师','地下城与勇士','穿越火线']
#1.贪婪模式
p = re.compile('<div><p>(.*)</p></div>',re.S)
r_list = p.findall(html)
print(r_list)
#2.非贪婪模式
p = re.compile('<div><p>(.*?)</p></div>',re.S)
r_list = p.findall(html)
print(r_list)