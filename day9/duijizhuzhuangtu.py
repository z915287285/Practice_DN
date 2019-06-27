import matplotlib as mpl
import matplotlib.pyplot as plt
##条形图
mpl.rcParams['font.sans-serif'] = ['SimHei']#font setting
mpl.rcParams['axes.unicode_minus'] = False #mode select

x = [1,2,3,4,5]
y = [6,5,7,1,10]
y1 = [2,6,3,8,5]
#align 对齐方式
plt.bar(x,y,align='center',color='b',tick_label=['A','B','C','D','E'],label='班级A',alpha = 0.6)
plt.bar(x,y1,align='center',bottom=y,color='#8da0cb',label='班级B',alpha = 0.6)
plt.xlabel('测试难度')
plt.ylabel('试卷份数')

plt.grid(True,axis='y',ls=':',color='r',alpha=0.3)
plt.show()