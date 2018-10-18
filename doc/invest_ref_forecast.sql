-- auto-generated definition
create table invest_ref_forecast
(
  `index`     INT(10)      null,
  code     VARCHAR(10)  null
  comment '股票代码',
  name     VARCHAR(10)  null
  comment '股票名称',
  type     VARCHAR(50)  null
  comment '业绩变动类型【预增、预亏等】',
  report_date        VARCHAR(50)  null
  comment '发布日期',
  pre_eps     VARCHAR(50)  null
  comment '上年同期每股收益',
  rangex     VARCHAR(50)  null
  comment '业绩变动范围'
)comment='
业绩预告
按年度、季度获取业绩预告数据，接口提供从1998年以后每年的业绩预告数据，
需指定年度、季度两个参数';
