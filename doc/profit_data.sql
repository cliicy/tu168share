-- auto-generated definition
create table profit_data
(
  `index`     INT(10)      null,
  code     VARCHAR(10)  null
  comment '股票代码',
  name     VARCHAR(10)  null
  comment '股票名称',
  roe     VARCHAR(10)  null
  comment '净资产收益率(%)',
  net_profit_ratio        VARCHAR(10)  null
  comment '净利率(%)',
  gross_profit_rate     VARCHAR(10)  null
  comment '毛利率(%)',
  net_profits     VARCHAR(10)  null
  comment '净利润(万元)',
  esp     VARCHAR(10)  null
  comment '每股收益',
  business_income        VARCHAR(100)  null
  comment '营业收入(百万元)',
  bips        VARCHAR(10)  null
  comment '每股主营业务收入(元)'
);