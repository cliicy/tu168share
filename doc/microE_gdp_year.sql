-- auto-generated definition
create table gdp_year
(
  `index`     INT(10)      null,
  year        VARCHAR(10)  null
  comment        '统计年度',
  gdp         VARCHAR(50)  null
  comment '国内生产总值(亿元)',
  pc_gdp         VARCHAR(50)  null
  comment '人均国内生产总值(元)',
  gnp         VARCHAR(50)  null
  comment '国民生产总值(亿元)',
  pi         VARCHAR(50)  null
  comment '第一产业(亿元)',
  si         VARCHAR(50)  null
  comment '第二产业(亿元)',
  industry         VARCHAR(50)  null
  comment '工业(亿元)',
  cons_industry          VARCHAR(50)  null
  comment '建筑业(亿元)',
  ti         VARCHAR(50)  null
  comment '第三产业(亿元)',
  trans_industry           VARCHAR(50)  null
  comment '交通运输仓储邮电通信业(亿元)',
  lbdy          VARCHAR(50)  null
  comment '批发零售贸易及餐饮业(亿元)'
)comment='
国内生产总值(年度)';
