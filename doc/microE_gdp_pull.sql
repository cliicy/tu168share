-- auto-generated definition
create table gdp_pull
(
  `index`     INT(10)      null,
  year        VARCHAR(10)  null
  comment        '统计年度',
  gdp_yoy          VARCHAR(50)  null
  comment '国内生产总值同比增长(%)',
  pi         VARCHAR(50)  null
  comment '第一产业拉动率(%)',
  si         VARCHAR(50)  null
  comment '第二产业拉动率(%)',
  industry         VARCHAR(50)  null
  comment '其中工业拉动(%)',
  ti         VARCHAR(50)  null
  comment '第三产业拉动率(%)'
)comment='
三大产业对GDP拉动';
