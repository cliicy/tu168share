-- auto-generated definition
create table invest_ref_sh_margin_details
(
  `index`     INT(10)      null,
  opDate     VARCHAR(50)  null
  comment '信用交易日期',
  stockCode     VARCHAR(10)  null
  comment '标的证券代码',
  securityAbbr     VARCHAR(10)  null
  comment '标的证券简称',
  rzye     VARCHAR(50)  null
  comment '本日融资余额(元)',
  rzmre        VARCHAR(50)  null
  comment '本日融资买入额(元)',
  rzche     VARCHAR(50)  null
  comment '本日融资偿还额',
  rqyl     VARCHAR(50)  null
  comment '本日融券余量',
  rqmcl     VARCHAR(50)  null
  comment '本日融券卖出量',
  rqchl     VARCHAR(50)  null
  comment '本日融券偿还量'
)comment='
融资融券（沪市）
沪市融资融券明细数据';
