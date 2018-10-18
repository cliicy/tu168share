-- auto-generated definition
create table rrr
(
  `index`     INT(10)      null,
  date        VARCHAR(50)  null
  comment        '变动日期',
  beforex       VARCHAR(50)  null
  comment '调整前存款准备金率(%)',
  now      VARCHAR(50)  null
  comment '调整后存款准备金率(%)',
  changed      VARCHAR(50)  null
  comment '调整幅度(%)'
)comment='
存款准备金率';
