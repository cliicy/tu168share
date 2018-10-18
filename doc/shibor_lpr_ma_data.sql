-- auto-generated definition
create table shibor_lpr_ma_data
(
  `index`     INT(10)      null,
  date        VARCHAR(50)  null
  comment        '发布日期',
  1Y_5     VARCHAR(50)  null
  comment '5日贷款基础利率均值',
  1Y_10     VARCHAR(50)  null
  comment '10日贷款基础利率均值',
  1Y_20     VARCHAR(50)  null
  comment '20日贷款基础利率均值'
)comment='
LPR均值数据
获取贷款基础利率均值数据，目前只提供2013年以来的数据。';
