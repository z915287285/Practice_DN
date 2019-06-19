
##手动清屏幕
# def clear():
#     for i in range(10):
#         print('')
stulist=[]
while True:
    #打印菜单
    # clear()
    print("1.添加一个新名字")
    print("2.删除一个名字")
    print("3.修改一个名字")
    print("4.查询一个名字")
    print("5.退出系统")
    print("0.显示所有已添加名字")
    opt=eval(input("请输入菜单序号："))
    if opt==1:
        new_name=input("请输入需要添加的姓名：")
        if stulist.count(new_name):
            print("用户名重复，请重新输入！！")
        else:
            stulist.append(new_name)
            print("添加成功！")
        continue
    elif opt==2:
        name=input("请输入你需要删除的姓名：")
        if stulist.count(name):
            index=stulist.index(name)
            stulist.pop(index)
            print("删除成功！")
        else:
            print("该用户不存在")
        continue
    elif opt==3:
        name=input("请输入需要修改的姓名：")
        if stulist.count(name):
            index=stulist.index(name)
            new_name=input("请输入新名字：")
            stulist[index]=new_name
            print("修改成功！！")
        else:
            print("该用户不存在")
        continue
    elif opt==4:
        qur_name = input("请输入需要查询的姓名：")
        if stulist.count(qur_name):
            index=stulist.index(qur_name)
            print("查询结果：",stulist[index])
        else:
            print("该用户不存在")
        continue
    elif opt==5:
        break
    elif opt ==0:
        if len(stulist)==0:
            print("当前还没有数据")
        else:
            for i in stulist:
                print(i)
        continue
    else:
        print("错误操作，请输入正确指令！！")
