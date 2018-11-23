#Author:immortal luo
# -*-coding:utf-8 -*-
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,DATE
from sqlalchemy.orm import sessionmaker


engine = create_engine("mysql+pymysql://root:csk1314520@localhost/oldboydb",
                       encoding='utf-8',echo=False)#echo:打印过程

Base = declarative_base()#生成ORM基类

class User(Base):
    __tablename__ = 'user'#表名
    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

    def __repr__(self):
        return "<%s name:%s>" % (self.id, self.name)

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer,primary_key=True)
    name = Column(String(32),nullable=False)
    age = Column(Integer,nullable=False)
    register_date = Column(DATE,nullable=False)

    def __repr__(self):
        return "<%s name:%s>"% (self.id,self.name)

Base.metadata.create_all(engine)#创建表结构



Session_class = sessionmaker(bind=engine)#创建与数据库的会话session 上课，注意这里返回给session的是个class。不是实例
Session = Session_class()#生成session实例，类似cursor
# user_obj = User(name='root',password='csk1314520')#生成你要创建的数据对象
# user_obj2 = User(name='csk',password='csk1314520')#生成你要创建的数据对象
# print(user_obj.name,user_obj.id)#此时还没创建对象，打印id发现输出None
#
# Session.add(user_obj)#把要创建的数据对象添加到这个session里，一会统一创建
# Session.add(user_obj2)#把要创建的数据对象添加到这个session里，一会统一创建
# print(user_obj.name,user_obj.id)#此时依然还没创建

# data = Session.query(User).filter_by(name='csk').all()
# data = Session.query(User).filter_by().all()
# data = Session.query(User).filter(User.id>1).filter(User.id<3).all()#多条件查询
# print(data[0].name,data[0].password)
# print(data)

# Session.rollback()#回滚


# print(Session.query(User,Student).filter(User.id==Student.id).all())
# print(Session.query(User).join(Student).all())#两表之间本来就有外键关系的情况下使用


# s1 = Student(name="pan",age=20,register_date="2018-5-6")
# Session.add(s1)
Session.commit()#现在才统一提交，创建数据

