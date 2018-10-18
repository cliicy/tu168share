-- auto-generated definition
create table shibor_quote_data
(
  `index`     INT(10)      null,
  date        VARCHAR(50)  null
  comment        '发布日期',
  bank     VARCHAR(10)  null
  comment '报价银行名称',
  ONx     VARCHAR(10)  null
  comment '隔夜拆放利率',
  ON_B     VARCHAR(10)  null
  comment '隔夜拆放买入价',
  ON_A     VARCHAR(10)  null
  comment '隔夜拆放卖出价',
  1W_B     VARCHAR(50)  null
  comment '1周买入',
  1W_A     VARCHAR(50)  null
  comment '1周卖出',
  2W_B        VARCHAR(50)  null
  comment '2周买入',
  2W_A       VARCHAR(50)  null
  comment '2周卖出',
  1M_B     VARCHAR(50)  null
  comment '1月买入',
  1M_A     VARCHAR(50)  null
  comment '1月卖出',
  3M_B     VARCHAR(50)  null
  comment '3月买入',
  3M_A     VARCHAR(50)  null
  comment '3月卖出',
  6M_B     VARCHAR(50)  null
  comment '6月买入',
  6M_A     VARCHAR(50)  null
  comment '6月卖出',
  9M_B     VARCHAR(50)  null
  comment '9月买入',
  9M_A     VARCHAR(50)  null
  comment '9月卖出',
  1Y_B     VARCHAR(50)  null
  comment '1年买入',
  1Y_A     VARCHAR(50)  null
  comment '1年卖出'
)comment='
银行报价数据
获取银行间报价数据，目前只提供2006年以来的数据。';
