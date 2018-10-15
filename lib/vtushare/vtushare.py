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

    def stock_basic(self):
        print('stock_basic')
        stock_bs.get_info()

    def k1m_sync(self):
        print('sync kline: 1M')

    def __list_all_member(self):
        for name in dir(self):
            print(name)





