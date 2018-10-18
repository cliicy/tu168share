-- auto-generated definition
create table gdp_for
(
  `index`     INT(10)      null,
  year         VARCHAR(10)  null
  comment        '统计年度',
  end_for          VARCHAR(50)  null
  comment '最终消费支出贡献率(%)',
  for_rate           VARCHAR(50)  null
  comment '最终消费支出拉动(百分点)',
  asset_for           VARCHAR(50)  null
  comment '资本形成总额贡献率(%)',
  asset_rate         VARCHAR(50)  null
  comment '资本形成总额拉动(百分点)',
  goods_for          VARCHAR(50)  null
  comment '货物和服务净出口贡献率(%)',
  goods_rate           VARCHAR(50)  null
  comment '货物和服务净出口拉动(百分点)'
)comment='
三大需求对GDP贡献';
