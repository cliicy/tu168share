-- auto-generated definition
create table invest_ref_sz_margin_details
(
  `index`     INT(10)      null,
  stockCode     VARCHAR(50)  null
  comment '标的证券代码',
  securityAbbr     VARCHAR(50)  null
  comment '标的证券简称',
  rzmre        VARCHAR(50)  null
  comment '本日融资买入额(元)',
  rzye     VARCHAR(50)  null
  comment '本日融资余额(元)',
  rqmcl     VARCHAR(50)  null
  comment '本日融券卖出量',
  rqyl     VARCHAR(50)  null
  comment '本日融券余量',
  rqye     VARCHAR(50)  null
  comment '本日融融券余量(元)',
  rzrqye     VARCHAR(50)  null
  comment '本日融资融券余额(元)',
  opDate     VARCHAR(50)  null
  comment '信用交易日期'
)comment='
融资融券（深市）
深市融资融券明细数据'
;