#coding=utf-8

import tushare as ts
from lib.vtushare.db.DbHelper import DbHelper

db = DbHelper()
session = db.getsession()
engine = db.getengine()


def get_info():
    # df = ts.get_h_data('600848')
    df = ts.get_h_data('600848', start='2018-08-01', end='2018-10-15')
    df.insert(0, 'ts_code', '600848')

    all_data_table_name = 'data_stock'
    # 写入数据库
    res = df.to_sql(all_data_table_name, engine, if_exists='append')

    # 三元表达式
    msg = 'ok' if res is None else res
    print(msg)
