st=input("请输入：")
a=[i for i in st]
b=dict.fromkeys(a,0)
for i in b:
    num=a.count(i)
    b[i]=num
for key,value in dict.items(b):
    print('%s:%d次'%(key,value))

s=input("请输入:")
d={}
for ch in  s:
    #判断这个字符串以前是否出现
    if ch not in d:#第一次出现
            d[ch]=1#将次数设置为1
    else:#不是第一次出现
        d[ch]+=1
#打印字符和出现过的次数
for k in d:
    print(k,':',d[k],'次')