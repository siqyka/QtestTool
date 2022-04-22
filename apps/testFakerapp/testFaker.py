import pymysql
from telnetlib import PRAGMA_HEARTBEAT
import os
import json
from .config import *
import hashlib
import datetime

tpath = os.path.dirname(os.path.realpath(__file__))
json_path = os.path.join(tpath, "fakerjson", "test.json")
now_time=datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d %H:%M:%S')

def connmysql():
    conn = pymysql.connect(host=host,  # 连接名称，默认127.0.0.1
                        user=user,  # 用户名
                        passwd=passwd,  # 密码
                        port=port,  # 端口，默认为3306
                        db=db,  # 数据库名称
                        charset=charset,  # 字符编码
                        cursorclass=cursorclass
                        )
    cur = conn.cursor()  # 生成游标对象
    return cur,conn

def closemysql(cur,conn):
    cur.close()  # 关闭游标
    conn.close()  # 关闭连接

def get_tfs():
    # 连接数据库
    cur,conn=connmysql()
    sql = "select pkey,path,returnstr from {} where alive='1';".format(table)  # SQL语句
    cur.execute(sql)  # 执行SQL语句
    data = cur.fetchall()  # 通过fetchall方法获得数据
    closemysql(cur,conn)
    return data

def modify_tf(pkey,path,text):
    try:
        cur,conn=connmysql()
        
        if pkey:
            sql="update {}.{} set `path`='{}',returnstr='{}', update_Time='{}' where pkey='{}';".format(db,table,path,text,now_time,pkey)
            cur.execute(sql)  # 执行SQL语句
            conn.commit()
        else:
            ssql="select pkey from {}.{} where path='{}' and alive='1';".format(db,table,path)
            print(ssql)
            cur.execute(ssql)  # 执行SQL语句
            data = cur.fetchone()  # 通过fetchall方法获得数据
            if data:
                return "T102"  # T102:路径已经存在
            hashv=path+now_time
            hashv=hashlib.sha1(hashv.encode()).hexdigest()
            sql = "INSERT INTO {}.{} (`path`, returnstr, pkey, insert_time) VALUES('{}', '{}', '{}', '{}');".format(db,table,path,text,hashv,now_time)  # SQL语句
            cur.execute(sql)  # 执行SQL语句
            conn.commit()
        closemysql(cur,conn)
        return True
    except:
        return False
    
def delete_tf(pkey):
    try:
        cur,conn=connmysql()
        sql="update {}.{} set alive='0',update_Time='{}' where pkey='{}';".format(db,table,now_time,pkey)
        cur.execute(sql)  # 执行SQL语句
        conn.commit()
        closemysql(cur,conn)
        return True
    except:
        return False
    
    
def tf_faker(path):
    try:
        cur,conn=connmysql()
        sql="select returnstr from {}.{} where path='{}' and alive='1';".format(db,table,path)
        cur.execute(sql)  # 执行SQL语句

        data = cur.fetchone()  # 通过fetchall方法获得数据
        closemysql(cur,conn)
        return data["returnstr"]
    except:
        return "False"


