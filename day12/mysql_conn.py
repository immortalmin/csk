#Author:immortal luo
# -*-coding:utf-8 -*-
import pymysql

# 创建连接
conn= pymysql.connect(host='localhost',port=3306,user='root',passwd='csk1314520',db='oldboydb')

#创建游标
cursor = conn.cursor()

#执行SQL，并返回受影响行数
# effect_row = cursor.execute("select * from student")

# print(cursor.fetchone())#取一条数据
# print(cursor.fetchall())#取所有（剩下所有）数据

# 提交，不然无法保存新建或者修改的数据


data = [
    ("shunli",21,'2011-5-4'),
    ("zhangjinmu",22,'2010-5-4'),
    ("lishujiang",23,'2011-6-4'),
    ("weijinyan",20,'2016-6-4')
]
cursor.executemany("insert into student (name,age,register_date) values(%s,%s,%s)",data)

conn.commit()

# 关闭游标

cursor.close()

#断开连接
conn.close()