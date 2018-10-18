-- auto-generated definition
create table lbh_inst_tops
(
  `index`     INT(10)      null,
  code     VARCHAR(10)  null
  comment '股票代码',
  name     VARCHAR(10)  null
  comment '股票名称',
  bamount        VARCHAR(50)  null
  comment '累积购买额(万)',
  bcount     VARCHAR(50)  null
  comment '买入次数',
  samount        VARCHAR(50)  null
  comment '累积卖出额(万)',
  scount     VARCHAR(50)  null
  comment '卖出次数',
  net     VARCHAR(50)  null
  comment '净额(万)'
)comment='
机构席位追踪
获取机构近5、10、30、60日累积买卖次数和金额等情况';
