-- auto-generated definition
create table new_stock
(
  `index`     INT(10)      null,
  code     VARCHAR(10)  null
  comment '股票代码',
  xcode        VARCHAR(10)  null
  comment '申购代码',
  name     VARCHAR(10)  null
  comment '股票名称',
  ipo_date     datetime  null
  comment '上网发行日期',
  issue_date     datetime  null
  comment '上市日期',
  amount        VARCHAR(10)  null
  comment '发行数量(万股)',
  markets        VARCHAR(10)  null
  comment '上网发行数量(万股)',
  price        VARCHAR(10)  null
  comment '发行价格(元)',
  pe        VARCHAR(10)  null
  comment '发行市盈率',
  limitx        VARCHAR(10)  null
  comment '个人申购上限(万股)',
  funds        VARCHAR(10)  null
  comment '募集资金(亿元)',
  ballot        VARCHAR(10)  null
  comment '网上中签率(%)'
);
