#
#
# # month check
# month=eval(input())
# if 1<=month and month <=12:
#     print("月份合理")
# else:
#     print("月份不合法")
#
#
# # face progress
# print("请输入年龄：")
# face_year=eval(input())
# print("请输入性别：（Male or Female）")
# face_gender=input()
#
# if 0<face_year<50 and face_gender =='Male':
#     print("允许面试")
# else:
#     print("不符合面试要求")


# print(0 and 0.01) # 优先返回假之对象
# print(0 or 0.1) # 优先返回真对象
#
# str1='helloworld'
# str2='abcd'
# str3='aaaaaa'
# print('%10s'%str1)
# print('%10s'%str2)
# print('%10s'%str3)

num=1
# while(num<=20):
#     print(num)
#     num=num+1

# while(num<=20):
#     print(num)
#     print(' ')
#     num=num+1
# row=6
# for i in range(row):
#     print(i)
#     col=0
#     while(0<=col+(row-i)<row):
#         print('*',end='')
#         col=col+1
#     print('')

s='  njsndnsa  slkdnalskd  skdnal'
count=0
for i in s:
    if i==' ':
        count+=1
count1=0
j=0
while j<len(s):
    if s[j]==' ':
        count1+=1
    j+=1

print(count)
print(count1)
print(s.count(' '))