#coding=utf-8

import sys
import lib.vtushare.tushare.stock_basic as stock_bs


class Tushare(object):

    __version = '0.1.0'

    def run(self):
        argv = sys.argv
        if len(argv) <= 1:
            self.help()
        else:
            method = sys.argv[1]

            if hasattr(self, method):
                method = getattr(self, method)
                method()
            else:
                self.help()

    def version(self):
        print(self.__version)

    def help(self):
        print('help')
        # print(dir(self))
        print(self.__list_all_member())

    def get_h_data(self):
        print('stock_basic')
        stock_bs.get_h_info()

    def stock_basic(self):
        print('stock_basic')
        stock_bs.update_stock_basic()

    def industry_info(self):
        print('get industry classified')
        stock_bs.get_industry_info()

    def k1m_sync(self):
        print('sync kline: 1M')

    def __list_all_member(self):
        for name in dir(self):
            print(name)

    def fq_data(self):
        print('get fq data')
        stock_bs.get_hfq_info()
        # stock_bs.get_fq_data()




