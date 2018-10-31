#
DIRECTORY STRUCTURE
-------------------
token: 47031bcac94db67f2ff5fd1afbf59c754fae3524438b1dbe048fba5b
```
/
    conf                配置
    doc                 相关文档
    test                测试/调试
    venv/               虚拟环境
    README.md           readme.md
    modules.txt         需要安装的模块
```

## 虚拟环境

```python
//激活虚拟环境
$ python3 -m venv venv(环境名称)
$ source bin/activate

// 退出虚拟环境
$ deactivate
```

## 相关扩展
* pip install XXX
* pip install -r filename
```
sqlalchemy
bs4
tushare
```

## 相关文档
* tushare: https://tushare.pro/document/2
https://tushare.pro/document/1?doc_id=40 调取PRO版数据
http://stock.eastmoney.com/report.html

# TO BE CONTINUED


运行命令行：
pushd f:\Projects\vTrade\vtushare\crawl_tu\crawl_tu\spiders
scrapy crawl today_money_flow > today_money_flow.txt