-- auto-generated definition
create table lbh_top_list
(
  `index`     INT(10)      null,
  code     VARCHAR(10)  null
  comment '股票代码',
  name     VARCHAR(10)  null
  comment '股票名称',
  pchange     VARCHAR(50)  null
  comment '当日涨跌幅',
  amount        VARCHAR(50)  null
  comment '龙虎榜成交额(万)',
  buy     VARCHAR(50)  null
  comment '买入额(万)',
  bratio     VARCHAR(50)  null
  comment '买入占总成交比例',
  sell     VARCHAR(50)  null
  comment '卖出额(万)',
  sratio     VARCHAR(50)  null
  comment '卖出占总成交比例',
  reason     VARCHAR(50)  null
  comment '上榜原因',
  date        VARCHAR(50)  null
  comment        '发布日期'
)comment='
每日龙虎榜列表
按日期获取历史当日上榜的个股数据，如果一个股票有多个上榜原因，则会出现该股票多条数据';
