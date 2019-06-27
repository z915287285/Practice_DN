import matplotlib as mpl
import matplotlib.pyplot as plt
##条形图
mpl.rcParams['font.sans-serif'] = ['SimHei']#font setting
mpl.rcParams['axes.unicode_minus'] = False #mode select

x = [1,2,3,4,5]
y = [6,5,7,1,10]
#align 对齐方式
plt.barh(x,y,align='center',color='c',tick_label=['A','B','C','D','E'],alpha = 0.6)

plt.xlabel('测试难度')
plt.ylabel('试卷份数')

plt.grid(True,axis='x',ls=':',color='r',alpha=0.3)
plt.show()