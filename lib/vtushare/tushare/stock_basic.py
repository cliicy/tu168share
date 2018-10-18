#coding=utf-8
import pandas as pd
import tushare as ts
from lib.vtushare.db.DbHelper import DbHelper
from conf.tushare import token

all_stocks_table_name = 'stock_industry'
table_stock_basic = 'stock_basic'
table_stock_data = 'data_stock'
hfq_k_data = 'hfq_k_data'
qfq_k_data = 'qfq_k_data'
table_hfq_stock_data = 'hfq_data_stock'
table_index_stock = 'stock_index'
all_concept_table = 'concept_classify'
all_area_table = 'area_classify'
all_sme_table = 'sem_classify'
all_gme_table = 'gem_classify'
all_st_table = 'st_classify'
all_hs300_table = 'hs300_classify'
all_zz500_table = 'zz500_classify'
all_sz50_table = 'sz50_classify'
all_suspended_table = 'suspended_classify'
all_terminated_table = 'terminated_classify'
all_new_stock_table = 'new_stock'
quarter_stock_report_table = 'report_data'
quarter_stock_profit_table = 'profit_data'
quarter_stock_operation_table = 'operation_data'
quarter_stock_growth_table = 'growth_data'
quarter_stock_debt_paying_table = 'debtpaying_data'
quarter_stock_cash_flow_table = 'cashflow_data'
invest_stock_ref_profit = 'invest_ref_profit'
invest_stock_ref_forecast = 'invest_ref_forecast'
invest_stock_ref_xsg = 'invest_ref_xsg_data'
invest_stock_ref_sh_margins = 'invest_ref_sh_margins'
invest_stock_ref_sh_margin_details = 'invest_ref_sh_margin_details'
invest_stock_ref_fund_holdings = 'invest_ref_fund_holdings'
invest_stock_ref_sz_margins = 'invest_ref_sz_margins'
invest_stock_ref_sz_margin_details = 'invest_ref_sz_margin_details'
lbh_top_list = 'lbh_top_list'
lbh_inst_detail = 'lbh_inst_detail'
lbh_inst_tops = 'lbh_inst_tops'
lbh_broker_tops = 'lbh_broker_tops'
lbh_cap_tops = 'lbh_cap_tops'

shibor_data = 'shibor_data'
shibor_quote_data = 'shibor_quote_data'
shibor_ma_data = 'shibor_ma_data'
shibor_lpr_ma_data = 'shibor_lpr_ma_data'
shibor_lpr_data = 'shibor_lpr_data'

microE_deposit_rate = 'deposit_rate'
microE_loan_rate = 'loan_rate'
microE_rrr = 'rrr'
microE_money_supply = 'money_supply'
microE_money_supply_bal = 'money_supply_bal'
microE_gdp_year = 'gdp_year'
microE_gdp_quarter = 'gdp_quarter'
microE_gdp_for = 'gdp_for'
microE_gdp_pull = 'gdp_pull'
microE_gdp_contrib = 'gdp_contrib'
microE_cpi = 'cpi'
microE_ppi = 'ppi'

fun_realtime_box_office = 'realtime_boxoffice'
fun_day_box_office = 'day_boxoffice'
fun_month_box_office = 'month_boxoffice'
fun_day_cinema = 'day_cinema'

ts.set_token(token)
pro = ts.pro_api()

db = DbHelper()
session = db.getsession()
engine = db.getengine()


def update_stock_basic():
    # 股票列表
    fields = 'ts_code,symbol,name,fullname,enname,exchange_id,curr_type,list_status,list_date,delist_date,is_hs'
    df = pro.stock_basic(fields=fields)
    # 写入数据库
    res = df.to_sql(table_stock_basic, engine, if_exists='replace')
    # 三元表达式
    msg = 'ok' if res is None else res
    print(msg)


def get_industry_info():
    # 行业分类
    df = ts.get_industry_classified()
    # 写入数据库
    res = df.to_sql('stock_industry', engine, if_exists='replace')
    # 三元表达式
    msg = 'ok' if res is None else res
    print('获取行业分类: ' + msg + '\n')


def get_concept_info():
    # 概念分类
    df = ts.get_concept_classified()
    # 写入数据库
    res = df.to_sql(all_concept_table, engine, if_exists='replace')
    # 三元表达式
    msg = 'ok' if res is None else res
    print('获取概念分类: ' + msg + '\n')
    print(msg)


def get_arealist_info():
    # 地域分类
    df = ts.get_area_classified()
    # 写入数据库
    res = df.to_sql(all_area_table, engine, if_exists='replace')
    # 三元表达式
    msg = 'ok' if res is None else res
    print('获取地域分类: ' + msg + '\n')
    print(msg)


def get_h_info():
    df1 = pd.read_sql(all_stocks_table_name, engine)
    for scode in df1['code']:
        # print(scode)
        df = ts.get_h_data(scode, start='2018-01-01', end='2018-10-15')
        df.insert(0, 'ts_code', scode)
        # 写入数据库
        res = df.to_sql(table_stock_data, engine, if_exists='replace')
        # 三元表达式
        msg = 'ok' if res is None else res
        print('write ' + scode + ' to history data table: '+msg+'\n')


def get_hfq_info():
    df1 = pd.read_sql(all_stocks_table_name, engine)
    for scode in df1['code']:
        # print(scode)
        df = ts.get_h_data(scode, start='2018-01-01', end='2018-10-15', autype='hfq')
        df.insert(0, 'ts_code', scode)
        df.rename(columns={'open': 'fopen', 'close': 'fclose', 'high': 'fhigh', 'low': 'flow'}, inplace=True)
        # 写入数据库
        res = df.to_sql(table_hfq_stock_data, engine, if_exists='replace')

        # 三元表达式
        msg = 'ok' if res is None else res
        print('write ' + scode + ' to 后复权 历史数据: '+msg+'\n')


def get_stock_index():
    """
    获取大盘指数行情
    return
    """
    # df1 = pd.read_sql(all_stocks_table_name, engine)
    # for scode in df1['code']:
    #     # print(scode)
    #     df = ts.get_h_data(scode, start='2018-01-01', end='2018-10-15', autype='hfq')
    #     df.insert(0, 'ts_code', scode)
    df = ts.get_index()
    # 写入数据库
    res = df.to_sql(table_index_stock, engine, if_exists='replace')
    # 三元表达式
    msg = 'ok' if res is None else res
    print('写入大盘指数行情: ' + msg + '\n')


def get_fq_data():
    dfs = pd.read_sql(table_stock_basic, engine)
    # 查询每只股票的上市日期
    for code in dfs['symbol']:
        print(code)
        dh = ts.get_k_data(code, autype='qfq')  # 不复权或前复权
        # print('{0} {1}'.format('前复权数据: ', dh))
        res = dh.to_sql(qfq_k_data, engine, if_exists='replace')
        # 三元表达式
        msg = 'ok' if res is None else res
        print('write ' + code + ' 前复权K数据: ' + msg + '\n')
        dg = ts.get_k_data(code, autype='hfq')  # 后复权
        # print('{0} {1}'.format('后复权数据: ', dg))
        dg.rename(columns={'open': 'fopen', 'close': 'fclose', 'high': 'fhigh', 'low': 'flow'}, inplace=True)
        res = dg.to_sql(hfq_k_data, engine, if_exists='replace')
        # 三元表达式
        msg = 'ok' if res is None else res
        print('write ' + code + ' 后复权K数据: ' + msg + '\n')
        # sql = "select list_date from {1} where symbol = '{0}'".format(code, table_stock_basic)
        # ld = pd.read_sql(sql, engine)  # 上市日期YYYYMMDD
        # for date in ld['list_date']:
        #     # print(date)
        #     date = formatdate(str(date), 'YYYY-MM-DD')  # 改一下格式
        #     # dh = ts.get_k_data(code, start='1990-01-01', end=date,  autype='qfq')  # 不复权或前复权
        #     dh = ts.get_k_data(code, autype='qfq')  # 不复权或前复权
        #     # dg = ts.get_k_data(code, start='1990-01-01', end=date, autype='hfq')  # 后复权
        #     dg = ts.get_k_data(code, autype='hfq')  # 后复权
    return
    dfs = pd.read_sql(table_stock_data, engine)
    # 查询每只股票的上市日期
    for code in dfs['ts_code']:
        print(code)
        # dh = ts.get_k_data(code, start='1990-01-01', end=date,  autype='qfq')  # 不复权或前复权
        dh = ts.get_k_data(code, autype='qfq')  # 不复权或前复权
        # dg = ts.get_k_data(code, start='1990-01-01', end=date, autype='hfq')  # 后复权
        dg = ts.get_k_data(code, autype='hfq')  # 后复权
        # merge_column = pd.concat([dh, dg], axis=1)
        # merge_column.to_sql('history', engine, if_exists='replace')
        # dg = ts.get_h_data(item, autype='hfq')  # 后复权
        # dh = ts.get_h_data(item, autype='qfq')  # 不复权
        # print('前复权数据' + '\n')
        print(dh)
        # print('后复权数据' + '\n')
        print(dg)


# 日期格式YYYYMMDD转为YYYY-MM-DD
def formatdate(date, format_type='YYYYMMDD'):
    format_type = format_type.replace('YYYY', date[0:4])
    format_type = format_type.replace('MM', date[4:6])
    format_type = format_type.replace('DD', date[-2:])
    return format_type


def get_sme_info():
    # 中小板分类
    df = ts.get_sme_classified()
    # 写入数据库
    res = df.to_sql(all_sme_table, engine, if_exists='replace')
    # 三元表达式
    msg = 'ok' if res is None else res
    print('获取中小板分类: ' + msg + '\n')
    print(msg)


def get_gme_info():
    # 创业板分类
    df = ts.get_gem_classified()
    # 写入数据库
    res = df.to_sql(all_gme_table, engine, if_exists='replace')
    # 三元表达式
    msg = 'ok' if res is None else res
    print('获取创业板分类: ' + msg + '\n')
    print(msg)


def get_st_info():
    # 风险警示板分类
    df = ts.get_st_classified()
    # 写入数据库
    res = df.to_sql(all_st_table, engine, if_exists='replace')
    # 三元表达式
    msg = 'ok' if res is None else res
    print('获取风险警示板分类: ' + msg + '\n')
    print(msg)


def get_hs300_info():
    # 沪深300当前成份股及所占权重
    df = ts.get_hs300s()
    # 写入数据库
    res = df.to_sql(all_hs300_table, engine, if_exists='replace')
    # 三元表达式
    msg = 'ok' if res is None else res
    print('获取沪深300当前成份股及所占权重: ' + msg + '\n')
    print(msg)


def get_sz50s_info():
    # 上证50成份股
    df = ts.get_sz50s()
    # 写入数据库
    res = df.to_sql(all_sz50_table, engine, if_exists='replace')
    # 三元表达式
    msg = 'ok' if res is None else res
    print('获取上证50成份股: ' + msg + '\n')
    print(msg)


def get_zz500s_info():
    # 中证500成份股
    df = ts.get_zz500s()
    print(df)
    return
    # 写入数据库
    res = df.to_sql(all_zz500_table, engine, if_exists='replace')
    # 三元表达式
    msg = 'ok' if res is None else res
    print('获取中证500成份股: ' + msg + '\n')
    print(msg)


def get_terminated_info():
    # 已经被终止上市的股票列表
    df = ts.get_terminated()
    # 写入数据库
    res = df.to_sql(all_terminated_table, engine, if_exists='replace')
    # 三元表达式
    msg = 'ok' if res is None else res
    print('获取已经被终止上市的股票列表: ' + msg + '\n')
    print(msg)


def get_suspended_info():
    # 被暂停上市的股票列表
    df = ts.get_suspended()
    df
    if df is None:
        return
    # 写入数据库
    res = df.to_sql(all_suspended_table, engine, if_exists='replace')
    # 三元表达式
    msg = 'ok' if res is None else res
    print('获取被暂停上市的股票列表: ' + msg + '\n')
    print(msg)


def get_new_stock_info():
    df = ts.new_stocks()
    # print(df)
    if df is not None:
        # 写入数据库
        res = df.to_sql(all_new_stock_table, engine, if_exists='replace')
        # 三元表达式
        msg = 'ok' if res is None else res
        print('获取新股数据: ' + msg + '\n')
        print(msg)


def get_report_info(year, quarter):
    """
            获取业绩报表数据
        Parameters
        --------
        year:int 年度 e.g:2014
        quarter:int 季度 :1、2、3、4，只能输入这4个季度
           说明：由于是从网站获取的数据，需要一页页抓取，速度取决于您当前网络速度
    """
    df = ts.get_report_data(year, quarter)
    print(df)
    if df is not None:
        # 写入数据库
        res = df.to_sql(quarter_stock_report_table, engine, if_exists='replace')
        # 三元表达式
        msg = 'ok' if res is None else res
        print('获取业绩报表数据: {0} {1}: {2}'.format(year, quarter, msg) + '\n')


def get_profit_info(year, quarter):
    """
    获取盈利能力数据
    Parameters
    --------
    year:int 年度 e.g:2014
    quarter:int 季度 :1、2、3、4，只能输入这4个季度
    """
    df = ts.get_profit_data(year, quarter)
    print(df)
    if df is not None:
        # 写入数据库
        res = df.to_sql(quarter_stock_profit_table, engine, if_exists='replace')
        # 三元表达式
        msg = 'ok' if res is None else res
        print('获取盈利能力数据: {0} {1}: {2}'.format(year, quarter, msg) + '\n')


def get_operation_info(year, quarter):
    """
    营运能力
    按年度、季度获取营运能力数据
    Parameters
    --------
    year:int 年度 e.g:2014
    quarter:int 季度 :1、2、3、4，只能输入这4个季度
    """
    df = ts.get_operation_data(year, quarter)
    print(df)
    if df is not None:
        # 写入数据库
        res = df.to_sql(quarter_stock_operation_table, engine, if_exists='replace')
        # 三元表达式
        msg = 'ok' if res is None else res
        print('获取营运能力数据: {0} {1}: {2}'.format(year, quarter, msg) + '\n')


def get_growth_info(year, quarter):
    """
    获取成长能力数据
    Parameters
    --------
    year:int 年度 e.g:2014
    quarter:int 季度 :1、2、3、4，只能输入这4个季度
    """
    df = ts.get_growth_data(year, quarter)
    print(df)
    if df is not None:
        # 写入数据库
        res = df.to_sql(quarter_stock_growth_table, engine, if_exists='replace')
        # 三元表达式
        msg = 'ok' if res is None else res
        print('获取成长能力数据: {0} {1}: {2}'.format(year, quarter, msg) + '\n')


def get_debt_paying_info(year, quarter):
    """
    获取偿债能力数据
    Parameters
    --------
    year:int 年度 e.g:2014
    quarter:int 季度 :1、2、3、4，只能输入这4个季度
    """
    df = ts.get_debtpaying_data(year, quarter)
    print(df)
    if df is not None:
        # 写入数据库
        res = df.to_sql(quarter_stock_debt_paying_table, engine, if_exists='replace')
        # 三元表达式
        msg = 'ok' if res is None else res
        print('获取偿债能力数据: {0} {1}: {2}'.format(year, quarter, msg) + '\n')


def get_cash_flow_info(year, quarter):
    """
    获取现金流量数据
    Parameters
    --------
    year:int 年度 e.g:2014
    quarter:int 季度 :1、2、3、4，只能输入这4个季度
    """
    df = ts.get_cashflow_data(year, quarter)
    print(df)
    if df is not None:
        # 写入数据库
        res = df.to_sql(quarter_stock_cash_flow_table, engine, if_exists='replace')
        # 三元表达式
        msg = 'ok' if res is None else res
        print('获取现金流量数据: {0} {1}: {2}'.format(year, quarter, msg) + '\n')


def get_ref_profit(year, top):
    """
    投资参考 系列
    分配预案：股票的送转和分红预案
    year : 预案公布的年份，默认为2014
    top :取最新n条数据，默认取最近公布的25条
    """
    df = ts.profit_data(year, top)
    print(df)
    if df is not None:
        # 写入数据库
        res = df.to_sql(invest_stock_ref_profit, engine, if_exists='replace')
        # 三元表达式
        msg = 'ok' if res is None else res
        print('获取股票的送转和分红预案数据: {0}: {1}'.format(year, msg) + '\n')


def get_ref_forecast_data(year, quarter):
    """
    投资参考 系列
    按年度、季度获取业绩预告数据，接口提供从1998年以后每年的业绩预告数据，
    需指定年度、季度两个参数
    """
    df = ts.forecast_data(year, quarter)
    print(df)
    if df is not None:
        # 写入数据库
        res = df.to_sql(invest_stock_ref_forecast, engine, if_exists='replace')
        # 三元表达式
        msg = 'ok' if res is None else res
        print('获取业绩预告数据: {0} {1}: {2}'.format(year, quarter, msg) + '\n')


def get_ref_xsg(year, month):
    """
    投资参考 系列
    以月的形式返回限售股解禁情况，通过了解解禁股本的大小，判断股票上行的压力。
    可通过设定年份和月份参数获取不同时段的数据
    """
    df = ts.xsg_data(year, month)
    print(df)
    if df is not None:
        # 写入数据库
        res = df.to_sql(invest_stock_ref_xsg, engine, if_exists='replace')
        # 三元表达式
        msg = 'ok' if res is None else res
        print('获取业绩预告数据: {0} {1}: {2}'.format(year, month, msg) + '\n')


def get_ref_fund_holdings(year, quarter):
    """
    投资参考 系列
    获取每个季度基金持有上市公司股票的数据
    """
    df = ts.fund_holdings(year, quarter)
    print(df)
    if df is not None:
        # 写入数据库
        res = df.to_sql(invest_stock_ref_fund_holdings, engine, if_exists='replace')
        # 三元表达式
        msg = 'ok' if res is None else res
        print('获取每个季度基金持有上市公司股票数据: {0} {1}: {2}'.format(year, quarter, msg) + '\n')


def get_sh_margins(start, end):
    """
    投资参考 系列
    融资融券（沪市）:沪市融资融券汇总数据
    """
    df = ts.sh_margins()
    # df = ts.sh_margins(start, end)
    print(df)
    if df is not None:
        # 写入数据库
        res = df.to_sql(invest_stock_ref_sh_margins, engine, if_exists='replace')
        # 三元表达式
        msg = 'ok' if res is None else res
        print('获取沪市融资融券汇总数据: 开始时间：{0} 结束时间：{1}: {2}'.format(start, end, msg) + '\n')


def get_sh_margin_details(start, end, symbol):
    """
    投资参考 系列
    融资融券（沪市）:沪市融资融券明细数据
    """
    # df = ts.sh_margin_details(start, end, symbol)
    df = ts.sh_margin_details()
    print(df)
    if df is not None:
        # 写入数据库
        res = df.to_sql(invest_stock_ref_sh_margin_details, engine, if_exists='replace')
        # 三元表达式
        msg = 'ok' if res is None else res
        print('获取沪市融资融券明细数据: 开始时间：{0} 结束时间：{1}: {2}'.format(start, end, msg) + '\n')


def get_sz_margins(start, end):
    """
    投资参考 系列
    融资融券（深市）:深市融资融券汇总数据
    """
    df = ts.sz_margins(start, end)
    print(df)
    if df is not None:
        # 写入数据库
        res = df.to_sql(invest_stock_ref_sz_margins, engine, if_exists='replace')
        # 三元表达式
        msg = 'ok' if res is None else res
        print('获取沪市融资融券汇总数据: 开始时间：{0} 结束时间：{1}: {2}'.format(start, end, msg) + '\n')


def get_sz_margin_details(start):
    """
    投资参考 系列
    融资融券（深市）:深市融资融券明细数据
    """
    df = ts.sz_margin_details(start)
    print(df)
    if df is not None:
        # 写入数据库
        res = df.to_sql(invest_stock_ref_sz_margin_details, engine, if_exists='replace')
        # 三元表达式
        msg = 'ok' if res is None else res
        print('获取沪市融资融券明细数据: 开始时间：{0}  {1}'.format(start, msg) + '\n')


def get_lbh_top_list(data):
    """
    按日期获取历史当日上榜的个股数据，
    如果一个股票有多个上榜原因，则会出现该股票多条数据
    """
    df = ts.top_list(data)
    print(df)
    if df is not None:
        # 写入数据库
        res = df.to_sql(lbh_top_list, engine, if_exists='replace')
        # 三元表达式
        msg = 'ok' if res is None else res
        print('获取历史当日上榜的个股数据: 开始时间：{0}  {1}'.format(data, msg) + '\n')


def get_lbh_inst_detail():
    """
    机构成交明细
    获取最近一个交易日机构席位成交明细统计数据
    """
    df = ts.inst_detail()
    print(df)
    if df is not None:
        # 写入数据库
        res = df.to_sql(lbh_inst_detail, engine, if_exists='replace')
        # 三元表达式
        msg = 'ok' if res is None else res
        print('获取最近一个交易日机构席位成交明细统计数据：{0}'.format(msg) + '\n')


def get_lbh_inst_tops(day):
    """
    机构席位追踪
    获取机构近5、10、30、60日累积买卖次数和金额等情况。
    """
    df = ts.inst_tops(day)
    print(df)
    if df is not None:
        # 写入数据库
        res = df.to_sql(lbh_inst_tops, engine, if_exists='replace')
        # 三元表达式
        msg = 'ok' if res is None else res
        print('获取机构近 {0} 日累积买卖次数和金额等情况：{1}'.format(day, msg) + '\n')


def get_lbh_broker_tops(day):
    """
    营业部上榜统计
    获取营业部近5、10、30、60日上榜次数、累积买卖等情况。
    """
    df = ts.broker_tops(day)
    print(df)
    if df is not None:
        # 写入数据库
        res = df.to_sql(lbh_broker_tops, engine, if_exists='replace')
        # 三元表达式
        msg = 'ok' if res is None else res
        print('获取营业部近 {0} 日上榜次数、累积买卖等情况：{1}'.format(day, msg) + '\n')


def get_lbh_cap_tops(day):
    """
    个股上榜统计
    获取近5、10、30、60日个股上榜统计数据,包括上榜次数、
    累积购买额、累积卖出额、净额、买入席位数和卖出席位数。
    """
    df = ts.cap_tops(day)
    print(df)
    if df is not None:
        # 写入数据库
        res = df.to_sql(lbh_cap_tops, engine, if_exists='replace')
        # 三元表达式
        msg = 'ok' if res is None else res
        print('获取近 {0} 日个股上榜统计数据,包括上榜次数、累积购买额、累积卖出额、净额、'
              '买入席位数和卖出席位数：{1}'.format(day, msg) + '\n')


def get_shibor_data(year):
    """
    Shibor拆放利率
    获取银行间同业拆放利率数据，目前只提供2006年以来的数据。
    """
    df = ts.shibor_data()
    # df = ts.shibor_data(year)
    print(df)
    if df is not None:
        # 写入数据库
        res = df.to_sql(shibor_data, engine, if_exists='replace')
        # 三元表达式
        msg = 'ok' if res is None else res
        print('获取银行间同业拆放利率数据: 年：{0}  {1}'.format(year, msg) + '\n')


def get_shibor_quote_data(year):
    """
    银行报价数据
    获取银行间报价数据，目前只提供2006年以来的数据。
    """
    df = ts.shibor_quote_data()
    # df = ts.shibor_quote_data(year)
    print(df)
    if df is not None:
        # 写入数据库
        res = df.to_sql(shibor_quote_data, engine, if_exists='replace')
        # 三元表达式
        msg = 'ok' if res is None else res
        print('获取银行间报价数据: 年：{0}  {1}'.format(year, msg) + '\n')


def get_shibor_ma_data(year):
    """
    获取Shibor均值数据，目前只提供2006年以来的数据。
    """
    df = ts.shibor_ma_data()
    # df = ts.shibor_ma_data(year)
    print(df)
    if df is not None:
        # 写入数据库
        res = df.to_sql(shibor_ma_data, engine, if_exists='replace')
        # 三元表达式
        msg = 'ok' if res is None else res
        print('获取Shibor均值数据: 年：{0}  {1}'.format(year, msg) + '\n')


def get_shibor_lpr_data(year):
    """
    贷款基础利率（LPR）
    获取贷款基础利率（LPR）数据，目前只提供2013年以来的数据。
    """
    df = ts.lpr_data()
    # df = ts.lpr_data(year)
    print(df)
    if df is not None:
        # 写入数据库
        res = df.to_sql(shibor_lpr_data, engine, if_exists='replace')
        # 三元表达式
        msg = 'ok' if res is None else res
        print('获取贷款基础利率（LPR）数据: 年：{0}  {1}'.format(year, msg) + '\n')


def get_shibor_lpr_ma_data(year):
    """
    LPR均值数据
    获取贷款基础利率均值数据，目前只提供2013年以来的数据。
    """
    df = ts.lpr_data()
    # df = ts.lpr_data(year)
    print(df)
    if df is not None:
        # 写入数据库
        res = df.to_sql(shibor_lpr_ma_data, engine, if_exists='replace')
        # 三元表达式
        msg = 'ok' if res is None else res
        print('获取贷款基础利率均值数据: 年：{0}  {1}'.format(year, msg) + '\n')


def get_deposit_rate_info():
    # 存款利率
    df = ts.get_deposit_rate()
    # 写入数据库
    res = df.to_sql(microE_deposit_rate, engine, if_exists='replace')
    # 三元表达式
    msg = 'ok' if res is None else res
    print('获取存款利率: ' + msg + '\n')


def get_loan_rate_info():
    # 贷款利率
    df = ts.get_loan_rate()
    # 写入数据库
    res = df.to_sql(microE_loan_rate, engine, if_exists='replace')
    # 三元表达式
    msg = 'ok' if res is None else res
    print('获取贷款利率: ' + msg + '\n')


def get_rrr_info():
    df = ts.get_rrr()
    # 写入数据库
    res = df.to_sql(microE_rrr, engine, if_exists='replace')
    # 三元表达式
    msg = 'ok' if res is None else res
    print('获取存款准备金率: ' + msg + '\n')


def get_money_supply_info():
    df = ts.get_money_supply()
    # 写入数据库
    res = df.to_sql(microE_money_supply, engine, if_exists='replace')
    # 三元表达式
    msg = 'ok' if res is None else res
    print('获取货币供应量: ' + msg + '\n')


def get_money_supply_bal_info():
    df = ts.get_money_supply_bal()
    # 写入数据库
    res = df.to_sql(microE_money_supply_bal, engine, if_exists='replace')
    # 三元表达式
    msg = 'ok' if res is None else res
    print('获取货币供应量(年底余额): ' + msg + '\n')


def get_gdp_year_info():
    df = ts.get_gdp_year()
    # 写入数据库
    res = df.to_sql(microE_gdp_year, engine, if_exists='replace')
    # 三元表达式
    msg = 'ok' if res is None else res
    print('获取国内生产总值(年度): ' + msg + '\n')


def get_gdp_quarter_info():
    df = ts.get_gdp_quarter()
    # 写入数据库
    res = df.to_sql(microE_gdp_quarter, engine, if_exists='replace')
    # 三元表达式
    msg = 'ok' if res is None else res
    print('获取国内生产总值(季度): ' + msg + '\n')


def get_gdp_for_info():
    df = ts.get_gdp_for()
    # 写入数据库
    res = df.to_sql(microE_gdp_for, engine, if_exists='replace')
    # 三元表达式
    msg = 'ok' if res is None else res
    print('获取三大需求对GDP贡献: ' + msg + '\n')


def get_gdp_pull_info():
    df = ts.get_gdp_pull()
    res = df.to_sql(microE_gdp_pull, engine, if_exists='replace')
    msg = 'ok' if res is None else res
    print('获取三大产业对GDP拉动: ' + msg + '\n')


def get_gdp_contrib_info():
    df = ts.get_gdp_contrib()
    res = df.to_sql(microE_gdp_contrib, engine, if_exists='replace')
    msg = 'ok' if res is None else res
    print('获取三大产业贡献率: ' + msg + '\n')


def get_gdp_cpi_info():
    df = ts.get_cpi()
    res = df.to_sql(microE_cpi, engine, if_exists='replace')
    msg = 'ok' if res is None else res
    print('获取居民消费价格指数: ' + msg + '\n')


def get_gdp_ppi_info():
    df = ts.get_ppi()
    res = df.to_sql(microE_ppi, engine, if_exists='replace')
    msg = 'ok' if res is None else res
    print('获取工业品出厂价格指数: ' + msg + '\n')


def get_realtime_boxoffice():
    df = ts.realtime_boxoffice()
    res = df.to_sql(fun_realtime_box_office, engine, if_exists='replace')
    msg = 'ok' if res is None else res
    print('获取获取实时电影票房数据: ' + msg + '\n')


def get_day_boxoffice(date=None):
    df = ts.day_boxoffice(date)
    res = df.to_sql(fun_day_box_office, engine, if_exists='replace')
    msg = 'ok' if res is None else res
    print('获取日期:{0} 电影票房数据:  {1} '.format(date, msg) + '\n')


def get_month_boxoffice(date=None):
    df = ts.month_boxoffice(date)
    res = df.to_sql(fun_month_box_office, engine, if_exists='replace')
    msg = 'ok' if res is None else res
    print('获取单月份：{0} 电影票房数据: {1} '.format(date, msg) + '\n')


def get_day_cinema(day=None):
    df = ts.day_cinema(day)
    res = df.to_sql(fun_day_cinema, engine, if_exists='replace')
    msg = 'ok' if res is None else res
    print('获取全国影院单日：{0}票房排行数据: {1} '.format(day, msg) + '\n')


if __name__ == "__main__":
    # 娱乐
    get_realtime_boxoffice()
    get_day_boxoffice()
    get_month_boxoffice('2018-08')
    get_day_cinema()
    # 娱乐
    # 宏观经济
    # get_deposit_rate_info()
    # get_loan_rate_info()
    # get_rrr_info()
    # get_money_supply_info()
    # get_gdp_contrib_info()
    # get_gdp_cpi_info()
    # get_gdp_year_info()
    # get_gdp_quarter_info()
    # get_gdp_for_info()
    # get_gdp_ppi_info()
    # get_gdp_pull_info()
    # get_gdp_for_info()
    # 宏观经济
    # get_shibor_data(2016)
    # get_shibor_quote_data(2017)
    # get_shibor_ma_data(2008)
    # get_shibor_lpr_ma_data(2017)

    # get_lbh_top_list('2018-08-01')
    # get_lbh_inst_detail()
    # get_lbh_inst_tops(60)
    # get_lbh_broker_tops(5)
    # get_lbh_cap_tops(10)
    # get_stock_index()
    # get_industry_info()
    # get_concept_info()
    # get_arealist_info()
    # get_sme_info()
    # get_gme_info()
    # get_st_info()
    # get_hs300_info()
    # get_terminated_info()
    # get_suspended_info()
    # get_zz500s_info()
    # get_sz50s_info()
    # get_new_stock_info()
    # get_report_info(2017, 3)
    # get_profit_info(2017, 3)
    # get_operation_info(2018, 1)
    # get_growth_info(2018, 1)
    # get_debt_paying_info(2018, 2)
    # get_cash_flow_info(2018, 2)
    # get_ref_profit(2017, 100)
    # get_ref_forecast_data(2018, 3)
    # get_ref_xsg(2018, 9)
    # get_ref_fund_holdings(2014, 3)
    # HTTP Error 403: Forbidden
    # get_sh_margins(start='2018-01-01', end='2018-09-30')
    # get_sh_margin_details(start='2018-08-01', end='2018-10-16', symbol='601989')
    #  HTTP Error 403: Forbidden

    # get_sz_margins(start='2018-08-01', end='2018-09-30')
    # get_sz_margin_details('2018-08-01')

    # get_fq_data()

