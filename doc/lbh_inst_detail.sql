-- auto-generated definition
create table lbh_inst_detail
(
  `index`     INT(10)      null,
  code     VARCHAR(10)  null
  comment '股票代码',
  name     VARCHAR(10)  null
  comment '股票名称',
  date        VARCHAR(50)  null
  comment        '交易日期',
  bamount        VARCHAR(50)  null
  comment '累积购买额(万)',
  samount        VARCHAR(50)  null
  comment '累积卖出额(万)',
  type     VARCHAR(50)  null
  comment '类型'
)comment='
机构成交明细
获取最近一个交易日机构席位成交明细统计数据';
