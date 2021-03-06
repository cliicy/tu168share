-- auto-generated definition
create table hfq_k_data
(
  `index`     VARCHAR(10)  null,
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
  code   VARCHAR(100)   null
  comment '成交金额'
)comment='
复权类型，qfq-前复权 hfq-后复权 None-不复权，默认为qfq';