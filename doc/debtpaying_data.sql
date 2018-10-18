-- auto-generated definition
create table debtpaying_data
(
  `index`     INT(10)      null,
  code     VARCHAR(10)  null
  comment '股票代码',
  name     VARCHAR(10)  null
  comment '股票名称',
  currentratio     VARCHAR(50)  null
  comment '流动比率',
  quickratio        VARCHAR(50)  null
  comment '速动比率',
  cashratio     VARCHAR(50)  null
  comment '现金比率',
  icratio     VARCHAR(50)  null
  comment '利息支付倍数',
  sheqratio     VARCHAR(50)  null
  comment '股东权益比率',
  adratio        VARCHAR(50)  null
  comment '股东权益增长率'
 )comment=
'
偿债能力
按年度、季度获取偿债能力数据，结果返回的数据属性说明如下：

code,代码
name,名称
currentratio,流动比率
quickratio,速动比率
cashratio,现金比率
icratio,利息支付倍数
sheqratio,股东权益比率
adratio,股东权益增长率
';