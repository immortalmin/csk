#Author:immortal luo
# -*-coding:utf-8 -*-

from sqlalchemy import Table,Column,Enum,Integer,String,DATE,ForeignKey,UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import ChoiceType,PasswordType

Base = declarative_base()



class Host(Base):
    __tablename__ = 'host'
    id = Column(Integer,primary_key=True)
    hostname = Column(String(64),unique=True)
    ip = Column(String(64),unique=True)
    port = Column(Integer,default=22)

    def __repr__(self):
        return self.hostname

class HostGroup(Base):
    __tablename__ = 'host_group'
    id = Column(Integer,primary_key=True)
    name = Column(String(64),unique=True)

    def __repr__(self):
        return self.name

class RemoteUser(Base):
    __tablename__ = 'remote_user'
    __table_args__ = (UniqueConstraint('auth_tupe','username','password',name='_user_passwd_uc'),)#联合唯一
    id = Column(Integer,primary_key=True)
    AuthTypes = [
        (u'ssh-passwd',u'SSH/Password'),#前者是实际存入数据库的数据，后者是显示给用户看的数据（映射关系）
        (u'ssh-key',u'SSH/KEY'),
    ]
    auth_type = Column(ChoiceType(AuthTypes))
    username = Column(String(32))
    password = Column(String(128))

    def __repr__(self):
        return self.username

class BindHost(Base):#用来表示user，

class UserProfile(Base):
    __tablename__ = 'user_profile'
    id = Column(Integer,primary_key=True)
    username = Column(String(32),unique=True)
    password = Column(String(128))

    def __repr__(self):
        return self.username