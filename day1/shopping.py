#Author:immortal luo
# -*-coding:utf-8 -*-

list1 = [["bike",800], ["luomin",100],["chenshengkuan",200],["zeng",300]]
minn = list1[0][1]
for i in list1:
    if(i[1]<minn):
        minn = i[1]
list2 =[]
salary = int(input("请输入你的工资:"))
while(True):
    # number = int(number)
    print("商品列表：")
    for i in list1:
        print(list1)

    number = input("请选择您要购买的商品，输入商品的商品编号:")
    if number.isdigit():
        number = int(number)
        if number>len(list1):
            print("输入的数字超出范围！")
            continue
        if salary<minn:
            print("购物清单：")
            for i in list2:
                print("商品：%s,价格：%d" %(i[0],i[1]))
            print("剩余余额：%d" %salary)
            break;
        if(list1[number-1][1]>salary):
            print("商品价格超出您的工资，无法购买！")
        else:
            salary -= list1[number-1][1]
            print("成功购买%s" %list1[number-1][0])
            print("剩余工资：%d" %salary)
            list2.append(list1[number-1])
    else:
        if(number == 'Q'):
            print("购物清单：")
            for i in list2:
                print("商品：%s,价格：%d" % (i[0], i[1]))
            print("剩余余额：%d" % salary)
            break;
        else:
            print("输入有误！如果要结账，请输入Q")