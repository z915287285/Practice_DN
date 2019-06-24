try:
    file1=open('myfile.txt','r',encoding='utf-8')
    print('打开文件成功')
    s=file1.readline()#读取一行，读到\n就返回
    print('读到',len(s),'个字符')
    print('内容是：',s)
    s=file1.readline()
    print('读到', len(s), '个字符')
    print('内容是：', s)
    s = file1.readline()
    print('读到', len(s), '个字符')
    print('内容是：', s)
#此处要进行读写
#关闭文件
    file1.close()
    print('文件关闭')
except OSError:
    print('打开文件失败')