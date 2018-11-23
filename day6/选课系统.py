#Author:immortal luo
# -*-coding:utf-8 -*-
import pickle

class School(object):#*********************学校*******************************
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        self.subject = []
        print("成功创建一所学校：%s"%self.name)
    def create_subject(self,subj,time,piece):#创建课程
        subje = Subject(subj,time,piece,self.addr)
        print("成功创建一门%s课程，上课地点在%s"%(subj,self.addr))
        self.subject.append(subje)

    def create_class(self,name,banzhuren,subj):#创建班级
        clas = Classroom(name,banzhuren,subj)
        print("成功创建一个班级：%s，班主任是:%s,地址在:%s"%(name,subj,self.addr))

class Subject(object):#*******************课程***************************
    def __init__(self,name,time,piece,where):
        self.name = name
        self.time = time
        self.piece = piece
        self.where = where

class Classroom(object):#*****************教室****************************
    def __init__(self,name,banzhuren,subj):
        self.name = name
        self.banzhuren = banzhuren
        self.subj = subj
        self.member = []
    def addmember(obj):#增加同学
        pass

class Student(object):#*********************学生*************************
    def __init__(self,name,classroom,subject,school):
        self.name = name
        self.classroom = classroom
        self.subject = subject
        self.school = school
        print("成功注册一名学生：%s"%self.name)


class Teacher(object):#***********************讲师***********************
    def __init__(self,name,age,classroom,subject,school):
        self.name = name
        self.age = age
        self.classroom = classroom
        self.subject = subject
        self.school = school

sc1 = School("北京大学","北京")
sc2 = School("复旦大学","上海")
sc1.create_subject("Linus",10,5000)
sc1.create_subject("Python",9,10000)
sc2.create_subject("Go",8,4000)
sc1.create_class("Python11期","alex","Python")
s1 = Student("陈盛款","Python11期","Python","北京大学")