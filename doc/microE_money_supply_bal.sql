-- auto-generated definition
create table money_supply_bal
(
  `index`     INT(10)      null,
  year        VARCHAR(10)  null
  comment        '统计年度',
  m2         VARCHAR(50)  null
  comment '货币和准货币（广义货币M2）(亿元)',
  m1         VARCHAR(50)  null
  comment '货币(狭义货币M1)(亿元)',
  m0         VARCHAR(50)  null
  comment '流通中现金(M0)(亿元)',
  cd         VARCHAR(50)  null
  comment '活期存款(亿元)',
  qm         VARCHAR(50)  null
  comment '准货币(亿元)',
  ftd         VARCHAR(50)  null
  comment '定期存款(亿元)',
  sd         VARCHAR(50)  null
  comment '储蓄存款(亿元)',
  rests         VARCHAR(50)  null
  comment '其他存款(亿元)'
)comment='
货币供应量(年底余额)';
