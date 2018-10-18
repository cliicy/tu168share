-- auto-generated definition
create table realtime_boxoffice
(
  `index`     INT(10)      null,
  BoxOffice         VARCHAR(10)  null
  comment        '实时票房（万）',
  Irank          VARCHAR(50)  null
  comment '排名',
  MovieName        VARCHAR(50)  null
  comment '影片名',
  boxPer         VARCHAR(50)  null
  comment '票房占比 （%）',
  movieDay         VARCHAR(50)  null
  comment '上映天数',
  sumBoxOffice        VARCHAR(50)  null
  comment '累计票房（万）',
  time         datetime  null
  comment '数据获取时间'
)comment='
实时票房
获取实时电影票房数据，30分钟更新一次票房数据，可随时调用';
