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

    def syn_all_info(self):
        print('update all data')
        # 娱乐
        stock_bs.get_realtime_boxoffice()
        stock_bs.get_day_boxoffice('2018-10-01')
        stock_bs.get_month_boxoffice('2018-08')
        stock_bs.get_day_cinema('2018-10-01')
        # 宏观经济
        stock_bs.get_deposit_rate_info()
        stock_bs.get_loan_rate_info()
        stock_bs.get_rrr_info()
        stock_bs.get_money_supply_info()
        stock_bs.get_gdp_contrib_info()
        stock_bs.get_gdp_cpi_info()
        stock_bs.get_gdp_year_info()
        stock_bs.get_gdp_quarter_info()
        stock_bs.get_gdp_for_info()
        stock_bs.get_gdp_ppi_info()
        stock_bs.get_gdp_pull_info()
        stock_bs.get_gdp_for_info()
        stock_bs.get_money_supply_bal_info()
        # 宏观经济
        for year in [2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]:
            stock_bs.get_shibor_data(year)
            stock_bs.get_shibor_quote_data(year)
        stock_bs.get_shibor_ma_data(2008)
        stock_bs.get_shibor_lpr_ma_data(2017)
        stock_bs.get_lbh_top_list('2018-08-01')
        stock_bs.get_lbh_inst_detail()
        stock_bs.get_lbh_inst_tops(60)
        stock_bs.get_lbh_broker_tops(5)
        stock_bs.get_lbh_cap_tops(10)
        stock_bs.get_stock_index()
        stock_bs.get_industry_info()
        stock_bs.get_concept_info()
        stock_bs.get_arealist_info()
        stock_bs.get_sme_info()
        stock_bs.get_gme_info()
        stock_bs.get_st_info()
        stock_bs.get_hs300_info()
        stock_bs.get_terminated_info()
        stock_bs.get_suspended_info()
        stock_bs.get_zz500s_info()
        stock_bs.get_sz50s_info()
        stock_bs.get_new_stock_info()
        stock_bs.get_report_info(2017, 3)
        stock_bs.get_profit_info(2017, 3)
        stock_bs.get_operation_info(2018, 1)
        stock_bs.get_growth_info(2018, 1)
        stock_bs.get_debt_paying_info(2018, 2)
        stock_bs.get_cash_flow_info(2018, 2)
        stock_bs.get_ref_profit(2017, 100)
        stock_bs.get_ref_forecast_data(2018, 3)
        stock_bs.get_ref_xsg(2018, 9)
        stock_bs.get_ref_fund_holdings(2014, 3)
        # HTTP Error 403: Forbidden
        # stock_bs.get_sh_margins()
        # stock_bs.get_sh_margin_details(symbol='601989')
        #  HTTP Error 403: Forbidden

        stock_bs.get_sz_margins(start='2018-08-01', end='2018-09-30')
        stock_bs.get_sz_margin_details('2018-08-01')

        stock_bs.get_fq_data()




