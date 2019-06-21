def get_op():
    s=input('请输入您要做的操作:')
    if s=='求最大':
        return max
    elif s=='求最小':
        return min
    elif s=='求和':
        return sum
L=[i for i in range(2,11,2)]
print(L)
f=get_op()
print(f(L))