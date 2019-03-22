import pymysql

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': '123456',
    'charset':'utf8mb4',
    'cursorclass':pymysql.cursors.DictCursor
    }
conn = pymysql.connect(**config)
conn.autocommit(1)
cursor = conn.cursor()

try:
    conn.select_db('bibodb2')
    cursor.execute('select id, related_links from bi_project_introduction')
    row = cursor.fetchone()
    print(row)
    import json 
    print(json.loads(row['related_links']))


    # 创建数据库
    DB_NAME = 'test'
    cursor.execute('DROP DATABASE IF EXISTS %s' % DB_NAME)
    cursor.execute('CREATE DATABASE IF NOT EXISTS %s' % DB_NAME)
    conn.select_db(DB_NAME)
    
    #创建表
    TABLE_NAME = 'user'
    cursor.execute('CREATE TABLE %s(id int primary key,name varchar(30))' % TABLE_NAME)
    
    # 批量插入纪录
    values = []
    for i in range(20):
        values.append((i,'su' + str(i)))
    cursor.executemany('INSERT INTO user values(%s,%s)',values)
    
    # 查询数据条目
    count = cursor.execute('SELECT * FROM %s' % TABLE_NAME)
    print('total records:', cursor.rowcount)
    
    # 获取表名信息
    desc = cursor.description
    print("cursor.description:%s %3s" % (desc[0][0], desc[1][0]))

    print("fetch one row {0}".format(cursor.fetchone()))
    print("fetch 3 rows {0}".format(cursor.fetchmany(3)))
    print("skip 10 rows")
    cursor.scroll(10,mode='relative')#absolute
    results = cursor.fetchall()
    for result in results:
        print(result)
        
except:
    import traceback
    traceback.print_exc()
    # 发生错误时会滚
    conn.rollback()
finally:
    # 关闭游标连接
    cursor.close()
    # 关闭数据库连接
    conn.close()
