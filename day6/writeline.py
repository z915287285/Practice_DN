try:
    f=open('mynote2.txt','w',encoding='utf-8')
    print('打开文件成功！')
    L=['你好','\n','ttt','sihuo','四火']
    f.writelines(L)
    f.close()
except OSError:
    print('打开文件失败!')
