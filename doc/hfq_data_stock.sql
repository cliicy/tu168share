-- auto-generated definition
create table hfq_data_stock
(
  `ts_code`     VARCHAR(10)  null
  comment '股票代码',
  date     datetime  null
  comment '交易日期',
  fopen      VARCHAR(10)   null
  comment '开盘价',
  fhigh        VARCHAR(10)  null
  comment '最高价',
  fclose    VARCHAR(10)  null
  comment '收盘价',
  flow      VARCHAR(10) null
  comment '最低价',
  volume VARCHAR(100)   null
  comment '成交量',
  amount   VARCHAR(100)   null
  comment '成交金额'
);

