
import pymysql
import redis

# MySQL数据库连接配置
mysql_config = {
    'host': '192.168.212.22',
    'user': 'dev',
    'password': 'dev@123',
    'db': 'myapp',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

# Redis连接配置
redis_config = {
    'host': '192.168.212.205',
    'port': 6379,
    'db': 0,
    'ssl': False,
    'health_check_interval': 30
}

def store_data_in_mysql(key, value):
    connection = pymysql.connect(**mysql_config)
    try:
        with connection.cursor() as cursor:
            # 插入或更新数据
            sql = "INSERT INTO data (key_name, value) VALUES (%s, %s) ON DUPLICATE KEY UPDATE value = VALUES(value)"
            cursor.execute(sql, (key, value))
        connection.commit()
    finally:
        connection.close()

def get_data(key):
    # 尝试从Redis中获取数据
    r = redis.Redis(**redis_config)
    cached_data = r.get(key)
    if cached_data is not None:
        return cached_data.decode('utf-8')
    
    # 如果Redis中没有数据，则从MySQL中获取
    connection = pymysql.connect(**mysql_config)
    try:
        with connection.cursor() as cursor:
            sql = "SELECT value FROM data WHERE key_name = %s"
            cursor.execute(sql, (key,))
            result = cursor.fetchone()
            if result:
                value = result['value']
                # 将数据缓存到Redis中，设置过期时间（例如，300秒）
                r.setex(key, 300, value)
                return value
    finally:
        connection.close()

if __name__ == '__main__':
    # 示例用法
    store_data_in_mysql('test', 'woshishui')
    data = get_data('test')
    print(data)
