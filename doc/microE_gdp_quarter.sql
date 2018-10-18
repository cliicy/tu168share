-- auto-generated definition
create table gdp_quarter
(
  `index`     INT(10)      null,
  quarter         VARCHAR(10)  null
  comment        '统计季度',
  gdp         VARCHAR(50)  null
  comment '国内生产总值(亿元)',
  gdp_yoy          VARCHAR(50)  null
  comment '国内生产总值同比增长(%)',
  pi          VARCHAR(50)  null
  comment '第一产业增加值(亿元)',
  pi_yoy         VARCHAR(50)  null
  comment '第一产业增加值同比增长(%)',
  si         VARCHAR(50)  null
  comment '第二产业增加值(亿元)',
  si_yoy          VARCHAR(50)  null
  comment '第二产业增加值同比增长(%)',
  ti         VARCHAR(50)  null
  comment '第三产业增加值(亿元)',
  ti_yoy           VARCHAR(50)  null
  comment '第三产业增加值同比增长(%)'
)comment='
国内生产总值(季度)';
