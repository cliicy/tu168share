-- auto-generated definition
create table cashflow_data
(
  `index`     INT(10)      null,
  code     VARCHAR(10)  null
  comment '股票代码',
  name     VARCHAR(10)  null
  comment '股票名称',
  cf_sales     VARCHAR(10)  null
  comment '经营现金净流量对销售收入比率',
  rateofreturn        VARCHAR(10)  null
  comment '资产的经营现金流量回报率',
  cf_nm     VARCHAR(10)  null
  comment '经营现金净流量与净利润的比率',
  cf_liabilities     VARCHAR(10)  null
  comment '经营现金净流量对负债比率',
  cashflowratio     VARCHAR(10)  null
  comment '现金流量比率'
 )comment=
'
现金流量
按年度、季度获取现金流量数据，结果返回的数据属性说明如下：

code,代码
name,名称
cf_sales,经营现金净流量对销售收入比率
rateofreturn,资产的经营现金流量回报率
cf_nm,经营现金净流量与净利润的比率
cf_liabilities,经营现金净流量对负债比率
cashflowratio,现金流量比率
';