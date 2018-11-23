#Author:immortal luo
# -*-coding:utf-8 -*-
info = {
    'stu1101': 'chenshengkuan',
    'stu1102': 'luomin',
    'stu1104': 'zeng',
    'stu1103': 'liushunli',
}
# print(info)
# print(info['stu1101'])#查找
# info['stu1101'] = 'huang'#增加
# del info['stu1101']#删除
# info.pop('stu1101')#删除

# print(info.get('stu1111'))
# print('stu1101' in info)#查找
# for i in info:
#     print(i,info[i])
for k,v in info.items():
    print(k,v)#上面的较高效