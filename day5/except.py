##except
def div_apple(n):
    print('%d个苹果您想分给几个人？'%n)
    s=input('请输入人数')
    cnt=int(s)
    result=n/cnt
    print('每个人分了%d个苹果'%result)
try:
    print('开始分苹果')
    div_apple(10)
    print('分苹果')
# except ValueError:
    # print('发生值错误，已处理并转为正常！！')
# except ZeroDivisionError:
    # print('发生了被零整除错误，程序已经转为正常！')
except (ValueError,ZeroDivisionError) as err:
    print('错误原因:',err)
    print('分苹果出现错误')
except:
    print('其他类型的错误')
else:
    print("程序正常运行并完成任务，正常退出")