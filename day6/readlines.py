try:
    file1=open('myfile.txt','r',encoding='utf-8')
    print('打开文件成功')
    s=file1.readlines()#读取所有行返回一个列表
    print('读到',len(s),'行')
    for index,i in enumerate(s):
        print('第',index+1,'行,内容是：',i)
#此处要进行读写
#关闭文件
    file1.close()
    print('文件关闭')
except OSError:
    print('打开文件失败')