# 实验五

### Task 1 使用SAE的MySQL服务

#### 任务要求：实现使用SAE的数据库服务，将之前实现的用户名密码登录的验证功能利用数据库来实现

新浪SAE提供了对MySQL数据库的支持，同时Python也有接入MySQL的库MySQLdb，因此可以在SAE上创建数据库，然后通过服务器程序对数据库进行简单的增删改查工作，实现一些相对具体的功能

#### SAE上MySQLdb的使用方法
在SAE上，创建数据库只需要在数据库的服务中点击开通即可，开通后SAE会自动生成数据库对应的host port username passwd dbname，也就是连接一个数据库需要的几个元素，这些元素都封装在了Python sae的库中，无需自己指定

model.py
```python
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
```

上面代码是简单的将新浪SAE的数据库服务和Python的MySQLdb模块的一个简单的封装，使用时只需要像下面这样调用即可
```python
from model import *
con = Connect()
res = Exec(con, 'XXX')
#res = Exec(con, 'select * from student')
```
只需要连接完数据库之后，就可以直接使用SQL语句进行操作了，接下来就是在数据库课程中学到的知识了

记得使用MySQLdb的时候，记得在config.yaml的文件中加上
```bash
- name: MySQLdb
  version: "1.2.3"
```