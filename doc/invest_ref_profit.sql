-- auto-generated definition
create table invest_ref_profit
(
  `index`     INT(10)      null,
  code     VARCHAR(10)  null
  comment '股票代码',
  name     VARCHAR(10)  null
  comment '股票名称',
  year     VARCHAR(10)  null
  comment '分配年份',
  report_date        VARCHAR(10)  null
  comment '公布日期',
  divi     VARCHAR(50)  null
  comment '分红金额（每10股）',
  shares     VARCHAR(50)  null
  comment '转增和送股数（每10股）'
)comment='
分配预案
每到季报、年报公布的时段，就经常会有上市公司利润分配预案发布';