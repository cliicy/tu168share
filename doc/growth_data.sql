-- auto-generated definition
create table growth_data
(
  `index`     INT(10)      null,
  code     VARCHAR(10)  null
  comment '股票代码',
  name     VARCHAR(10)  null
  comment '股票名称',
  mbrg     VARCHAR(50)  null
  comment '主营业务收入增长率(%)',
  nprg        VARCHAR(50)  null
  comment '净利润增长率(%)',
  nav     VARCHAR(50)  null
  comment '净资产增长率',
  targ     VARCHAR(50)  null
  comment '总资产增长率',
  epsg     VARCHAR(50)  null
  comment '每股收益增长率',
  seg        VARCHAR(50)  null
  comment '股东权益增长率'
)comment= 
'
成长能力
按年度、季度获取成长能力数据，结果返回的数据属性说明如下：

code,代码
name,名称
mbrg,主营业务收入增长率(%)
nprg,净利润增长率(%)
nav,净资产增长率
targ,总资产增长率
epsg,每股收益增长率
seg,股东权益增长率
';