stulist=[]
target=['name','age','wechat','phone']
b=dict.fromkeys(target,0)
while True:
    #打印菜单
    print("1.添加一个名片信息")
    print("2.删除一个名片")
    print("3.修改一个名片信息")
    print("4.查询一个名片信息")
    print("5.保存信息")
    print("6.退出系统")
    print("0.显示所有已添加名片所有信息")
    opt=eval(input("请输入菜单序号："))
    #判断操作序号
    if opt==1:
        new_name=input("请输入需要添加的姓名：")
        for st in stulist:
            if new_name == st['name']:
                print("用户名重复，请重新输入！！")
                break
        else:
            age=eval(input("请输入年龄："))
            wechat = input("请输入wechat：")
            phone = input("请输入phone：")
            b['name'] = new_name
            b['age'] = age
            b['wechat'] = wechat
            b['phone'] = phone
            stulist.append(b)
            b = dict.fromkeys(target, 0)
            print("添加成功！")
        continue
    elif opt==2:
        name=input("请输入你需要删除的姓名：")
        for st in stulist:
            if name == st['name']:
                a=stulist.index(st)
                stulist.pop(a)
                print("删除成功！")
                break
        else:
            print("该用户不存在")
        continue
    elif opt==3:
        ##打印二级菜单
        print("1.修改姓名")
        print("2.修改年龄")
        print("3.修改wechat")
        print("4.修改phone")
        print("5.修改所有信息")
        print("0.退出当前操作")
        opt1 = eval(input("请输入菜单序号："))
        if opt1!=0:
            name = input("请输入需要修改名片信息的姓名：")
            ##查找是否存在
            for st in stulist:
                if name == st['name']:
                    index = stulist.index(st)
                    break
            else:
                print("该用户不存在")
                continue
        if opt1 == 1:
            new_name = input("请输入新名字：")
            stulist[index]['name'] = new_name
            print("修改姓名成功！！")
            continue
        elif opt1 == 2:
            age = eval(input("请输入修改年龄："))
            stulist[index]['age'] = age
            print("修改年龄成功！！")
            continue
        elif opt1 == 3:
            wechat =input("请输入修改wechat：")
            stulist[index]['wechat'] = wechat
            print("修改wechat成功！！")
            break
        elif opt1 == 4:
            phone = input("请输入修改phone：")
            stulist[index]['phone'] = phone
            print("修改phone成功！！")
            continue
        elif opt1 == 5:
            new_name = input("请输入新名字：")
            age = eval(input("请输入修改年龄："))
            wechat = input("请输入新wechat：")
            phone = input("请输入新phone：")
            stulist[index]['name'] = new_name
            stulist[index]['age'] = age
            stulist[index]['wechat'] = wechat
            stulist[index]['phone'] = phone
            print("修改名片成功！！")
            continue
        elif opt1 == 0:
            continue
    elif opt==4:
        qur_name = input("请输入需要查询的姓名：")
        for st in stulist:
            if qur_name == st['name']:
                index=stulist.index(st)
                print('+-------+--------+-------+-------+')
                print('|  姓名 |  年龄  |  wechat  |  phone  |')
                print('+-------+--------+-------+-------+')
                print('|   %s  |   %d   |   %s  |   %s  |' \
                          % (stulist[index]['name'], stulist[index]['age'], stulist[index]['wechat'], stulist[index]['phone'],))
                print('+-------+--------+-------+')
        else:
            print("该用户不存在")
        continue
    elif opt==5:
        filename=input("输入需要存入的文本名:")
        st1=[]
        for i in stulist:
            a=['姓名:',i['name'],'\t年龄:',str(i['age']),'\t微信:',i['wechat'],'\t手机号码:',i['phone'],'\n']
            st1.append(a)
        try:
            f = open(filename+'.txt', 'w', encoding='utf-8')
            print('打开或创建文件成功！')
            for l in st1:
                f.writelines(l)
            f.close()
        except OSError:
            print('打开或创建文件失败!')
        continue
    elif opt==6:
        break
    elif opt ==0:
        if len(stulist)==0:
            print("当前还没有数据")
        else:
            print('+-------+--------+-------+-------+')
            print('|  姓名 |  年龄  |  wechat  |  phone  |')
            print('+-------+--------+-------+-------+')
            for i in range(len(stulist)):
                print('|   %s  |   %d   |   %s  |   %s  |' \
                      % (stulist[i]['name'], stulist[i]['age'], stulist[i]['wechat'],stulist[i]['phone'],))
            print('+-------+--------+-------+')
        continue
    else:
        print("错误操作，请输入正确指令！！")
