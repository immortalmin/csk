#Author:immortal luo
# -*-coding:utf-8 -*-
from day12 import ORM_many_fk
from sqlalchemy.orm import sessionmaker

Session_class = sessionmaker(bind=ORM_many_fk.engine)
session = Session_class()

# addr1 = ORM_many_fk.Address(street="Tiantongyuan",city="ChangPing",state="BeiJing")
# addr2 = ORM_many_fk.Address(street="Wudaokou",city="Haidian",state="BeiJing")
# addr3 = ORM_many_fk.Address(street="Yanjiao",city="Langfang",state="HeBei")
#
# session.add_all([addr1,addr2,addr3])
# c1 = ORM_many_fk.Customer(name="csk",billing_address=addr1,shipping_address=addr2)
# c2 = ORM_many_fk.Customer(name="lmm",billing_address=addr3,shipping_address=addr3)
#
# session.add_all([c1,c2])

obj = session.query(ORM_many_fk.Customer).filter(ORM_many_fk.Customer.name=="csk").first()
print(obj.name,obj.billing_address,obj.shipping_address)

session.commit()