-- auto-generated definition
create table loan_rate
(
  `index`     INT(10)      null,
  date        VARCHAR(50)  null
  comment        '执行日期',
  loan_type       VARCHAR(50)  null
  comment '存款种类',
  rate      VARCHAR(50)  null
  comment '利率（%）'
)comment='
贷款利率';
