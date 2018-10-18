-- auto-generated definition
create table money_supply
(
  `index`     INT(10)      null,
  month        VARCHAR(10)  null
  comment        '统计时间',
  m2         VARCHAR(50)  null
  comment '货币和准货币（广义货币M2）(亿元)',
  m2_yoy         VARCHAR(50)  null
  comment '货币和准货币（广义货币M2）同比增长(%)',
  m1         VARCHAR(50)  null
  comment '货币(狭义货币M1)(亿元)',
  m1_yoy         VARCHAR(50)  null
  comment '货币(狭义货币M1)同比增长(%)',
  m0         VARCHAR(50)  null
  comment '流通中现金(M0)(亿元)',
  m0_yoy         VARCHAR(50)  null
  comment '流通中现金(M0)同比增长(%)',
  cd         VARCHAR(50)  null
  comment '活期存款(亿元)',
  cd_yoy         VARCHAR(50)  null
  comment '活期存款同比增长(%)',
  qm         VARCHAR(50)  null
  comment '准货币(亿元)',
  qm_yoy         VARCHAR(50)  null
  comment '准货币同比增长(%)',
  ftd         VARCHAR(50)  null
  comment '定期存款(亿元)',
  ftd_yoy         VARCHAR(50)  null
  comment '定期存款同比增长(%)',
  sd         VARCHAR(50)  null
  comment '储蓄存款(亿元)',
  sd_yoy         VARCHAR(50)  null
  comment '储蓄存款同比增长(%)',
  rests         VARCHAR(50)  null
  comment '其他存款(亿元)',
  rests_yoy         VARCHAR(50)  null
  comment '其他存款同比增长'
)comment='
货币供应量';
