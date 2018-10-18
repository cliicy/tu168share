-- auto-generated definition
create table ppi
(
  `index`     INT(10)      null,
  month        VARCHAR(10)  null
  comment        '统计月份',
  ppiip         VARCHAR(50)  null
  comment '工业品出厂价格指数',
  ppi         VARCHAR(50)  null
  comment '生产资料价格指数',
  qm         VARCHAR(50)  null
  comment '采掘工业价格指数',
  rmi         VARCHAR(50)  null
  comment '原材料工业价格指数',
  pi         VARCHAR(50)  null
  comment '加工工业价格指数',
  cg         VARCHAR(50)  null
  comment '生活资料价格指数',
  food         VARCHAR(50)  null
  comment '食品类价格指数',
  clothing         VARCHAR(50)  null
  comment '衣着类价格指数',
  roeu         VARCHAR(50)  null
  comment '一般日用品价格指数',
  dcg         VARCHAR(50)  null
  comment '耐用消费品价格指数'
)comment='
工业品出厂价格指数';
