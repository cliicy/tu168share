-- auto-generated definition
create table operation_data
(
  `index`     INT(10)      null,
  code     VARCHAR(10)  null
  comment '股票代码',
  name     VARCHAR(10)  null
  comment '股票名称',
  arturnover     VARCHAR(50)  null
  comment '应收账款周转率(次)',
  arturndays        VARCHAR(100)  null
  comment '应收账款周转天数(天)',
  inventory_turnover     VARCHAR(50)  null
  comment '存货周转率(次)',
  inventory_days     VARCHAR(100)  null
  comment '存货周转天数(天)',
  currentasset_turnover     VARCHAR(10)  null
  comment '流动资产周转率(次)',
  currentasset_days        VARCHAR(100)  null
  comment '流动资产周转天数(天)'
 )comment=
'
营运能力
按年度、季度获取营运能力数据，结果返回的数据属性说明如下：

code,代码
name,名称
arturnover,应收账款周转率(次)
arturndays,应收账款周转天数(天)
inventory_turnover,存货周转率(次)
inventory_days,存货周转天数(天)
currentasset_turnover,流动资产周转率(次)
currentasset_days,流动资产周转天数(天)
';