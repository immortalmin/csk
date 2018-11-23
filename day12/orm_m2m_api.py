#Author:immortal luo
# -*-coding:utf-8 -*-
from day12 import orm_m2m
from sqlalchemy.orm import sessionmaker

Session_class = sessionmaker(bind=orm_m2m.engine)
session = Session_class()

# b1 = orm_m2m.Book(name="learn python with Alex",pub_date="2014-5-2")
# b2 = orm_m2m.Book(name="learn linux with Alex",pub_date="2010-8-2")
# b3 = orm_m2m.Book(name="learn PHP with Alex",pub_date="2011-5-5")
# b4 = orm_m2m.Book(name="learn 计算机 with Alex",pub_date="2011-5-5")
#
# a1 = orm_m2m.Author(name="Alex")
# a2 = orm_m2m.Author(name="Jack")
# a3 = orm_m2m.Author(name="Rain")

#
# b1.authors = [a1,a3]
# b3.authors = [a1,a2,a3]
#
# session.add_all([b1,b2,b3,a1,a2,a3])
# session.add(b4)

#*********************************************************************

#查询信息
# author_obj = session.query(orm_m2m.Author).filter(orm_m2m.Author.name=="alex").first()
# print(author_obj.books)

# book_obj = session.query(orm_m2m.Book).filter(orm_m2m.Book.id==2).first()
# print(book_obj.authors)
# book_obj.authors.remove(author_obj)
session.commit()