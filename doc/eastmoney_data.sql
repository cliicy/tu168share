-- auto-generated definition
create table eastmoney_data
(
  `index`     INT(10)      null,
  日期     datetime  null
  comment '日期',
  代码     VARCHAR(10)  null
  comment '股票代码',
  名称        VARCHAR(10)  null
  comment '企业名称',
  相关     VARCHAR(10)  null
  comment '详细信息',
  研报     VARCHAR(10)   null
  comment '研报：点评细节',
  原文评级 VARCHAR(10)  null
  comment '原文评级',
  评级变动     VARCHAR(10)   null
  comment '评级变动',
  机构     VARCHAR(10)   null
  comment '机构信息',
  2018预测收益    VARCHAR(10)   null
  comment '2018预测-收益',
  2018预测市盈率     VARCHAR(10)   null
  comment '2018预测-市盈率',
  2019预测收益     VARCHAR(10)   null
  comment '2019预测-收益',
  2019预测市盈率     VARCHAR(10)   null
  comment '2019预测-市盈率'
);


