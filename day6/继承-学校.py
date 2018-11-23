#Author:immortal luo
# -*-coding:utf-8 -*-

class School(object):
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.teacher = []
        self.staff = []

    def enroll(self,stu_obj):
        print("为学员%s办理注册手续"%stu_obj.name)
        self.students.append(stu_obj)

    def hire(self,staff_obj):
        print("雇佣新员工%s"%staff_obj.name)
        self.staff.append(staff_obj)

class SchoolMember(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def tell(self):
        pass

class Teacher(SchoolMember):
    def __init__(self,name,age,sex,salary,course):
        super(Teacher, self).__init__(name,age,sex)####
        self.salary = salary
        self.course = course

    def tell(self):
        print('''
        -----info of Teacher:%s------
        Name:%s
        Age:%s
        Sex:%s
        Salary:%s
        Course:%s
        '''%(self.name,self.name,self.age,self.sex,self.salary,self.course))

    def teach(self):
        print("%s is teaching course[%s]"%(self.name,self.course))

class Student(SchoolMember):
    def __init__(self,name,age,sex,stu_id,grade):
        super(Student, self).__init__(name,age,sex)
        self.stu_id = stu_id
        self.grade = grade

    def tell(self):
        print('''
        --------info of Student %s--------
        Name:%s
        Age:%s
        Sex:%s
        Stu_id:%s
        Grade:%s
        '''%(self.name,self.name,self.age,self.sex,self.stu_id,self.grade))

    def pay_tuition(self,amount):
        print("%s has paid tuition for $%s"%(self.name,amount))

school = School("老男孩IT","沙河")

t1 = Teacher("Oldboy",56,"MF",2000000,"Linux")
t2 = Teacher("Alex",22,"M",3000,"PythonDevOps")

s1 = Student("Chenshengkuan",19,"M","1716143101","python")
s2 = Student("luominmin",19,"F","1716143333","Spanish")

t1.tell()
s2.tell()
school.hire(t1)
school.enroll(s1)
# for i in school.students:
#     print(i.name)
#
# for i in school.staff:
#     print(i.name)
print(school.students)
print(school.staff)