-- auto-generated definition
create table invest_ref_fund_holdings
(
  `index`     INT(10)      null,
  CODE     VARCHAR(10)  null
  comment '股票代码',
  NAME     VARCHAR(10)  null
  comment '股票名称',
  date        VARCHAR(10)  null
  comment '报告日期',
  nums     VARCHAR(50)  null
  comment '基金家数',
  nlast     VARCHAR(50)  null
  comment '与上期相比（增加或减少了）',
  count     VARCHAR(10)  null
  comment '基金持股数（万股）',
  clast     VARCHAR(50)  null
  comment '与上期相比',
  amount     VARCHAR(50)  null
  comment '基金持股市值',
  ratio     VARCHAR(10)  null
  comment '占流通盘比率', 
  ESYMBOL     VARCHAR(10)  null,
  EXCHANGE        VARCHAR(10)  null,
  RN     VARCHAR(50)  null,
  SHANGQIGUSHU     VARCHAR(10)  null,
  SHANGQISHIZHI     VARCHAR(50)  null,
  SHANGQISHULIANG     VARCHAR(50)  null
)comment='
基金持股
获取每个季度基金持有上市公司股票的数据。'
;