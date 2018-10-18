-- auto-generated definition
create table lbh_cap_tops
(
  `index`     INT(10)      null,
  code     VARCHAR(10)  null
  comment '股票代码',
  name     VARCHAR(10)  null
  comment '股票名称',
  count     VARCHAR(50)  null
  comment '上榜次数',
  bamount        VARCHAR(50)  null
  comment '累积购买额(万)',
  samount        VARCHAR(50)  null
  comment '累积卖出额(万)',
  net     VARCHAR(50)  null
  comment '净额(万)',
  bcount     VARCHAR(50)  null
  comment '买入席位数',
  scount     VARCHAR(50)  null
  comment '卖出席位数'
)comment='
个股上榜统计
获取近5、10、30、60日个股上榜统计数据,
包括上榜次数、累积购买额、累积卖出额、净额、买入席位数和卖出席位数。';
