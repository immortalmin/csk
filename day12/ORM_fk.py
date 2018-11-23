#Author:immortal luo
# -*-coding:utf-8 -*-
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,DATE,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship


engine = create_engine("mysql+pymysql://root:csk1314520@localhost/oldboydb",
                       encoding='utf-8',echo=False)#echo:打印过程

Base = declarative_base()#生成ORM基类

class Student(Base):
    __tablename__ = "student"
    id = Column(Integer,primary_key=True)
    name = Column(String(32),nullable=False)
    register_date = Column(DATE,nullable=False)

    def __repr__(self):
        return "<%s name:%s>"%(self.id,self.name)

class StudyRecord(Base):
    __tablename__ = "study_record"
    id = Column(Integer,primary_key=True)
    day = Column(Integer,nullable=False)
    status = Column(String(32),nullable=False)
    stu_id = Column(Integer,ForeignKey("student.id"))

    student = relationship("Student",backref="my_study_record")

    def __repr__(self):
        return "<%s day:%s status:%s>" % (self.student.name,self.day,self.status)

Base.metadata.create_all(engine)#创建表结构

Session_class = sessionmaker(bind=engine)
session = Session_class()

# s1 = Student(name='csk',register_date='2015-5-6')
# s2 = Student(name='lmm',register_date='2016-5-16')
# s3 = Student(name='zeng',register_date='2005-4-6')
# s4 = Student(name='liu',register_date='2011-5-26')
#
# study_obj1 = StudyRecord(day=1,status='YES',stu_id=1)
# study_obj2 = StudyRecord(day=2,status='YES',stu_id=1)
# study_obj3 = StudyRecord(day=3,status='YES',stu_id=1)
# study_obj4 = StudyRecord(day=1,status='YES',stu_id=2)
#
# session.add_all([s1,s2,s3,s4,study_obj1,study_obj2,study_obj3,study_obj4])

stu_obj = session.query(Student).filter(Student.name=='csk').first()
# print(stu_obj)
print(stu_obj.my_study_record)
session.commit()