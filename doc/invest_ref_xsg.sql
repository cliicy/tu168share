-- auto-generated definition
create table invest_ref_xsg
(
  `index`     INT(10)      null,
  code     VARCHAR(10)  null
  comment '股票代码',
  name     VARCHAR(10)  null
  comment '股票名称',
  date        datetime  null
  comment '解禁日期',
  count     VARCHAR(10)  null
  comment '解禁数量（万股）',
  ratio     VARCHAR(10)  null
  comment '占总盘比率'
)comment='
限售股解禁
以月的形式返回限售股解禁情况，通过了解解禁股本的大小，判断股票上行的压力。可通过设定年份和月份参数获取不同时段的数据。'
;
