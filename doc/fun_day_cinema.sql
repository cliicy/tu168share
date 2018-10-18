-- auto-generated definition
create table day_cinema
(
  `index`     INT(10)      null,
  Attendance         VARCHAR(10)  null
  comment        '上座率',
  AvpPeoPle          VARCHAR(50)  null
  comment '场均人次',
  CinemaName        VARCHAR(50)  null
  comment '影院名称',
  RowNum         VARCHAR(50)  null
  comment '排名',
  TodayAudienceCount         VARCHAR(50)  null
  comment '当日观众人数',
  TodayBox        VARCHAR(50)  null
  comment '当日票房',
  TodayShowCount         VARCHAR(50)  null
  comment '当日场次',
  price         VARCHAR(50)  null
  comment '场均票价（元）'
)comment='
影院日度票房
获取全国影院单日票房排行数据，默认为上一日，可输入日期参数获取指定日期的数据。';
