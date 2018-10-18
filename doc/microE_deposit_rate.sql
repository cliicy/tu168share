-- auto-generated definition
create table deposit_rate
(
  `index`     INT(10)      null,
  date        VARCHAR(50)  null
  comment        '变动日期',
  deposit_type      VARCHAR(50)  null
  comment '存款种类',
  rate      VARCHAR(50)  null
  comment '利率'
)comment='
存款利率';
