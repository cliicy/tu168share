-- auto-generated definition
create table terminated_classify
(
  `index`     INT(10)      null,
  code     VARCHAR(10)  null
  comment '股票代码',
  name        VARCHAR(10)  null
  comment '股票名称',
  oDate     datetime  null
  comment '上市日期',
  tDate   VARCHAR(10)   null
  comment '终止上市日期'
);

