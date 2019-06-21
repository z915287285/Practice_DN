#3.globals/locals
a=1
b=1
c=3

def fn(c,d):
    e=33
    #此处有几个局部变量
    print('locals()返回:',locals())
    print('-----------------------')
    print('globals()返回:',globals())
    print('局部变量C的值是：',c)
    print('全局变量c值:',globals()['c'])

fn(100,200)
print('==========================')
print('全局的globals()返回',globals())