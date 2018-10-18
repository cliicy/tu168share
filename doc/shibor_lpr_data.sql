-- auto-generated definition
create table shibor_lpr_data
(
  `index`     INT(10)      null,
  date        VARCHAR(50)  null
  comment        '发布日期',
  1Y     VARCHAR(50)  null
  comment '1年贷款基础利率'
)comment='
贷款基础利率（LPR）
获取贷款基础利率（LPR）数据，目前只提供2013年以来的数据。';
