## 序列方法

inp=[]
while True:
    a=eval(input('请输入:'))
    if a<0:
        break
    else:
        inp.append(a)
        i+=1
print("列表是:",inp)
print("平均值是:",sum(inp)/len(inp))
print("最大值是:",max(inp))