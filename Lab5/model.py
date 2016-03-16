#-*-coding:utf-8-*-
import sae.const  #引入sae的常量
import MySQLdb

HOST = sae.const.MYSQL_HOST
USER = sae.const.MYSQL_USER
PASSWD = sae.const.MYSQL_PASS
DB = sae.const.MYSQL_DB
PORT = int(sae.const.MYSQL_PORT)
#以上几个赋值是将sae自带的几个常量提取出来

def Connect():
	#连接数据库
	con = MySQLdb.connect(host=HOST,user=USER,passwd=PASSWD,db=DB,port=PORT)
	return con

def Exec(con,query):
	#执行SQL语句
	cur = con.cursor()
	cur.execute(query)
	res = cur.fetchall()
	return res