-- auto-generated definition
create table shibor_ma_data
(
  `index`     INT(10)      null,
  date        VARCHAR(50)  null
  comment        '发布日期',
  ON_5     VARCHAR(10)  null
  comment '隔夜5日均值',
  ON_10     VARCHAR(10)  null
  comment '隔夜10日均值',
  ON_20     VARCHAR(10)  null
  comment '隔夜20日均值',
  1W_5     VARCHAR(50)  null
  comment '1周5日均值',
  1W_10     VARCHAR(50)  null
  comment '1周10日均值',
  1W_20        VARCHAR(50)  null
  comment '1周20日均值',
  2W_5       VARCHAR(50)  null
  comment '2周5日均值',
  2M_10     VARCHAR(50)  null
  comment '2周10日均值'
)comment='
Shibor均值数据
获取Shibor均值数据，目前只提供2006年以来的数据。';
