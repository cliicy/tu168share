#coding:utf-8

# python3 不支持 MySQL-python
import pymysql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from conf import db

pymysql.install_as_MySQLdb()
engine = create_engine(db.url)  # 创建引擎

DB_Session = sessionmaker(bind=engine)
session = DB_Session()
# session.execute("set names utf8")


class DbHelper:
    db_engine = None
    db_session = None

    def __init__(self):
        self.db_engine = engine
        self.db_session = session

    def getengine(self):
        return self.db_engine

    def getsession(self):
        return self.db_session
