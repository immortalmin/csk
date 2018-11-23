#Author:immortal luo
# -*-coding:utf-8 -*-
import pymysql

# 打开数据库连接
# db = pymysql.connect("localhost","testuser","test123","TESTDB" )

# 使用cursor()方法获取操作游标
# cursor = db.cursor()

# SQL 更新语句
# sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
# try:
   # 执行SQL语句
   # cursor.execute(sql)
   # 提交到数据库执行
   # db.commit()
# except:
   # 发生错误时回滚
   # db.rollback()

# 关闭数据库连接
# db.close()


#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql

# 创建连接
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='csk1314520', db='oldboydb')
# 创建游标
cursor = conn.cursor()

# 执行SQL，并返回收影响行数
effect_row = cursor.execute("update student set name='chen' where name='csk'")

# 执行SQL，并返回受影响行数
#effect_row = cursor.execute("update hosts set host = '1.1.1.2' where nid > %s", (1,))

# 执行SQL，并返回受影响行数
#effect_row = cursor.executemany("insert into hosts(host,color_id)values(%s,%s)", [("1.1.1.11",1),("1.1.1.11",2)])


# 提交，不然无法保存新建或者修改的数据
conn.commit()

# 关闭游标
cursor.close()
# 关闭连接
conn.close()