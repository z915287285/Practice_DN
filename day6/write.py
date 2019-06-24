try:
    f=open('mynote.txt','w',encoding='utf-8')
    #W代表写模式
    print('文件打开成功')
    f.write('hello')
    f.close()
except OSError:
    print('打开文件失败!')