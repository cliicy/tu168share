-- auto-generated definition
create table month_boxoffice
(
  `index`     INT(10)      null,
  IRank         VARCHAR(50)  null
  comment '排名',
  MovieName         VARCHAR(50)  null
  comment '影片名',
  WomIndex           VARCHAR(50)  null
  comment '口碑指数',
  avgboxoffice         VARCHAR(50)  null
  comment '平均票价',
  avgshowcount         VARCHAR(50)  null
  comment '场均人次',
  box_pro        VARCHAR(50)  null
  comment '月度占比',
  boxoffice          VARCHAR(50)  null
  comment '单月票房(万)',
  days        VARCHAR(50)  null
  comment '月内天数',
  releaseTime          datetime  null
  comment '上映日期'
)comment='
月度票房
获取单月电影票房数据，默认为上一月，可输入月份参数获取指定月度的数据。';
