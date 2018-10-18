-- auto-generated definition
create table lbh_broker_tops
(
  `index`     INT(10)      null,
  broker     VARCHAR(10)  null
  comment '营业部名称',
  count     VARCHAR(50)  null
  comment '上榜次数',
  bamount        VARCHAR(50)  null
  comment '累积购买额(万)',
  bcount        VARCHAR(50)  null
  comment '买入席位数',
  samount        VARCHAR(50)  null
  comment '累积卖出额(万)',
  scount     VARCHAR(50)  null
  comment '卖出席位数',
  top3        VARCHAR(50)  null
  comment '买入前三股票'
)comment='
营业部上榜统计
获取营业部近5、10、30、60日上榜次数、累积买卖等情况';
