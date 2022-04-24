import pymysql

host=''  # 连接名称，默认127.0.0.1
user= '' # 用户名
passwd=''  # 密码
port=3306  # 端口，默认为3306
db=''  # 数据库名称
charset='utf8'  # 字符编码
table=""
cursorclass=pymysql.cursors.DictCursor
