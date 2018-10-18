-- auto-generated definition
create table day_boxoffice
(
  `index`     INT(10)      null,
  AvgPrice         VARCHAR(10)  null
  comment        '平均票价',
  AvpPeoPle          VARCHAR(50)  null
  comment '场均人次',
  BoxOffice        VARCHAR(50)  null
  comment '单日票房（万）',
  BoxOffice_Up         VARCHAR(50)  null
  comment '环比变化 （%）',
  IRank         VARCHAR(50)  null
  comment '排名',
  MovieDay        VARCHAR(50)  null
  comment '上映天数',
  MovieName         VARCHAR(50)  null
  comment '影片名',
  SumBoxOffice         VARCHAR(50)  null
  comment '累计票房（万）',
  WomIndex        VARCHAR(50)  null
  comment '口碑指数'
)comment='
每日票房
获取单日电影票房数据，默认为上一日的电影票房，可输入参数获取指定日期的票房。';
