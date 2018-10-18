-- auto-generated definition
create table stock_index
(
  `index`     INT(10)      null,
  code     VARCHAR(10)  null
  comment '指数代码',
  name     VARCHAR(10)  null
  comment '指数名称',
  changex     VARCHAR(100) null
  comment '涨跌幅',
  open     VARCHAR(100) null
  comment '开盘价',
  preclose     VARCHAR(10)   null
  comment '昨日收盘价',
  close     VARCHAR(10)   null
  comment '收盘价',
  high     CHAR(10)      null
  comment '最高价',
  low     INT(10)      null
  comment '最低价',
  volume     VARCHAR(100)   null
  comment '成交量(手)',
  amount     VARCHAR(100)   null
  comment '成交金额（亿元）'
);

