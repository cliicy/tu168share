-- auto-generated definition
create table invest_ref_sh_margins
(
  `index`     INT(10)      null,
  opDate     VARCHAR(10)  null
  comment '信用交易日期',
  rzye     VARCHAR(10)  null
  comment '本日融资余额',
  rzmre        VARCHAR(10)  null
  comment '本日融资买入额',
  rqyl     VARCHAR(50)  null
  comment '本日融券余量',
  rqylje     VARCHAR(50)  null
  comment '本日融券余量金额',
  rqmcl     VARCHAR(10)  null
  comment '本日融券卖出量',
  rzrqjyzl     VARCHAR(50)  null
  comment '本日融资融券余额'
)comment='
融资融券（沪市）
沪市融资融券汇总数据'
;