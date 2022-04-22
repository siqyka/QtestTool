import pymysql

host='121.5.22.173'  # 连接名称，默认127.0.0.1
user='qiyk'  # 用户名
passwd='123456'  # 密码
port=3306  # 端口，默认为3306
db='qyktest'  # 数据库名称
charset='utf8'  # 字符编码
table="testfaker"
cursorclass=pymysql.cursors.DictCursor
