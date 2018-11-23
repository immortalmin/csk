#Author:immortal luo
# -*-coding:utf-8 -*-

name = "my \tname is csk"
print(name.capitalize())
print(name.count("s"))
print(name.center(50,"+"))#打印50个字符，不足50个的话，用“+”代替
print(name.endswith("cs"))#判断是否以“cs”结尾
print(name.expandtabs(tabsize=10))#将字符串中的tab键转换为10个空格
print(name.find("name"))#返回name的位置,可做切片
print(name[name.find("name"):9])#切片
name1 = "my name is {name},i am {age} years old"
print(name1.format(name='csk',age='19'))
print(name1.format_map({'name':'csk','age':19}))
print('ab12'.isalnum())#判断只包含英文字母和数字
print('asa'.isalpha())#判断是否只包含英文字母
print('123'.isdecimal())#判断是否只包含十进制数字
print('123'.isdigit())#判断是否是个整数
print('a123'.isidentifier())#判断是否是一个合法的标识符
print('aa'.islower())#是不是小写
print('12.3'.isnumeric())#是不是一个数字，小数点不行
print('','+'.join(['1','2','3']))#输出 1+2+3
print('   123  '.strip())#去两边的空格，还有rstrip,lstrip
p = str.maketrans("abcdefg",'1234567')
print("fjanbfajbf".translate(p))#替换，随机密码
print("123 123 123 1".split(' '))
#....
