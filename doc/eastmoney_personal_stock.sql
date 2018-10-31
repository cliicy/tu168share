-- auto-generated definition
create table eastmoney_personal_stock
(
  `index`     INT(10)      null,
  author     VARCHAR(10)   null
  comment 'author',
  change     VARCHAR(10)   null
  comment '发展反向： 比如 维持',
  companyCode     VARCHAR(10)   null
  comment '公司代码',
  datetime     VARCHAR(10)  null
  comment '时间： 比如 2018-10-25T06:59:45',
  infoCode     VARCHAR(10)  null
  comment 'info code: 比如 APPISDDNAIBXASearchReport',
  insCode        VARCHAR(10)  null
  comment 'insCode 企业代码 ',
  insName     VARCHAR(10)  null
  comment '企业名称',
  insStar     VARCHAR(10)   null
  comment '企业等级',
  jlrs VARCHAR(10)  null
  comment 'jlrs 比如 ['398820000', '540810000', '697400000', '', '']',
  rate     VARCHAR(10)   null
  comment '方向： 比如 买入',
  secuFullCode     VARCHAR(10)   null
  comment 'secuFullCode',
  secuName    VARCHAR(10)   null
  comment 'secuName',
  sratingName     VARCHAR(10)   null
  comment 'sratingName： 比如 买入',
  sy     VARCHAR(10)   null
  comment 'sy',
  syls     VARCHAR(10)   null
  comment 'syls: 比如 ['19.89', '14.67', '11.37', '', '']',
  sys     VARCHAR(10)   null
  comment 'sys: 比如 ['0.66', '0.9', '1.16', '', '']',
  sys     VARCHAR(10)   null
  comment 'sys: 比如 ['0.66', '0.9', '1.16', '', '']',
  title     VARCHAR(10)   null
  comment 'title',
  profitYear     VARCHAR(10)   null
  comment 'profitYear',
  type     VARCHAR(10)   null
  comment 'type',
  newPrice     VARCHAR(10)   null
  comment 'newPrice'
);
 {'author': '全铭,焦德智,许汪洋', 'change': '维持', 'companyCode': '80198452', 'datetime': '2018-10-25T07:01:52', 'infoCode': 'APPISDSMQmpdASearchReport', 'insCode': '80000031', 'insName': '东吴证券', 'insStar': '3', 'jlrs': ['254000000', '342000000', '465000000', '', ''], 'rate': '增持', 'secuFullCode': '300357.SZ', 'secuName': '我武生物', 'sratingName': '增持', 'sy': '1.1500', 'syls': ['40.72', '30.27', '22.28', '', ''], 'sys': ['0.87', '1.18', '1.6', '', ''], 'title': '收入增速31.36%，业绩符合预期，在研品种进展顺利', 'profitYear': '2017', 'type': '1', 'newPrice': '35.62'}
