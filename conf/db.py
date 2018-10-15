arr = {
    "host": '10.0.131.74',
    "user": 'root',
    "password": '1',
    "db": 'tushare',
    "port": 3306,
    "charset": 'utf8'
}

url = f"mysql://{arr['user']}:{arr['password']}@{arr['host']}"f":{arr['port']}/{arr['db']}?charset={arr['charset']}"
