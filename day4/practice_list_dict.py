target=['name','age','score']
b=dict.fromkeys(target,0)
total=[]
while True:
    name=input("请输入姓名:")
    if name=='':
        break
    age=eval(input("请输入年龄:"))
    score=eval(input("请输入分数:"))
    b['name']=name
    b['age']=age
    b['score']=score
    total.append(b)
    b = dict.fromkeys(target, 0)
print('+-------+--------+-------+')
print('|  姓名 |  年龄  |  成绩  |')
print('+-------+--------+-------+')
for i in range(len(total)):
    print('|   %s  |   %d   |   %d  |'\
          %(total[i]['name'],total[i]['age'],total[i]['score']))
print('+-------+--------+-------+')