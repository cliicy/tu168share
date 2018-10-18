arr = {
    "host": '172.24.132.208',
    "user": 'pig',
    "password": 'pig123',
    "db": 'tushare',
    "port": 3306,
    "charset": 'utf8'
}

url = f"mysql://{arr['user']}:{arr['password']}@{arr['host']}"f":{arr['port']}/{arr['db']}?charset={arr['charset']}"
