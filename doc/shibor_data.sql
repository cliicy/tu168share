-- auto-generated definition
create table shibor_data
(
  `index`     INT(10)      null,
  date        VARCHAR(50)  null
  comment        '发布日期',
  ONx     VARCHAR(10)  null
  comment '隔夜拆放利率',
  1W     VARCHAR(50)  null
  comment '1周拆放利率',
  2W        VARCHAR(50)  null
  comment '2周拆放利率',
  1M     VARCHAR(50)  null
  comment '1个月拆放利率',
  3M     VARCHAR(50)  null
  comment '3个月拆放利率',
  6M     VARCHAR(50)  null
  comment '6个月拆放利率',
  9M     VARCHAR(50)  null
  comment '9个月拆放利率',
  1Y     VARCHAR(50)  null
  comment '1年拆放利率'
)comment='
Shibor拆放利率
获取银行间同业拆放利率数据，目前只提供2006年以来的数据。';
