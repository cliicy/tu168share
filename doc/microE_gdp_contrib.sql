-- auto-generated definition
create table gdp_contrib
(
  `index`     INT(10)      null,
  year        VARCHAR(10)  null
  comment        '统计年度',
  gdp_yoy          VARCHAR(50)  null
  comment '国内生产总值',
  pi         VARCHAR(50)  null
  comment '第一产业贡献率(%)',
  si         VARCHAR(50)  null
  comment '第二产业贡献率(%)',
  industry         VARCHAR(50)  null
  comment '其中工业贡献率(%)',
  ti         VARCHAR(50)  null
  comment '第三产业贡献率(%)'
)comment='
三大产业贡献率';
