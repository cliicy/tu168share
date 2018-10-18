-- auto-generated definition
create table report_data
(
  `index`     INT(10)      null,
  code     VARCHAR(10)  null
  comment '股票代码',
  name     VARCHAR(10)  null
  comment '股票名称',
  eps     VARCHAR(10)  null
  comment '每股收益',
  eps_yoy     VARCHAR(10)  null
  comment '每股收益同比(%)',
  bvps     VARCHAR(10)  null
  comment '每股净资产',
  roe     VARCHAR(10)  null
  comment '净资产收益率(%)',
  epcf        VARCHAR(10)  null
  comment '每股现金流量(元)',
  net_profits        VARCHAR(10)  null
  comment '净利润(万元)',
  profits_yoy        VARCHAR(10)  null
  comment '净利润同比(%)',
  distrib        VARCHAR(10)  null
  comment '分配方案',
  report_date     VARCHAR(10)  null
  comment '发布日期'
);