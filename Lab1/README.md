# 实验一

## HTTP请求

HTTP(HyperText Transfer Protocol)是一套计算机通过网络进行通信的规则。计算机专家设计出HTTP，使HTTP客户（如Web浏览器）能够从HTTP服务器(Web服务器)请求信息和服务，HTTP目前协议的版本是1.1.HTTP是一种无状态的协议，无状态是指Web浏览器和Web服务器之间不需要建立持久的连接，这意味着当一个客户端向服务器端发出请求，然后Web服务器返回响应(response)，连接就被关闭了，在服务器端不保留连接的有关信息.HTTP遵循请求(Request)/应答(Response)模型。Web浏览器向Web服务器发送请求，Web服务器处理请求并返回适当的应答。所有HTTP连接都被构造成一套请求和应答。

### HTTP请求七步骤

- (1) 建立TCP连接
- (2) client向server发送HTTP请求
- (3) client发送header
- (4) server发送协议版本号及status_code
- (5) server发送应答header
- (6) server发送数据
- (7) server关闭TCP连接

### HTTP请求格式

- 请求方法：`GET` `POST` `PUT` `DELETE` CONNECT OPTIONS PATCH PROPFIND PROPPATCH MKCOL COPY MOVE LOCK UNLOCK TRACE HEAD
- 请求头：（包含许多有关的客户端环境和请求正文的有用信息）
    * Accept 
    * Accept-Language
    * Connection
    * User-Agent
    * Content-Length
    * [Content-type](http://tool.oschina.net/commons)
    * ...
- 请求正文：key1=value1&key2=value2&key3=value3的格式

### HTTP状态码

- 消息（1字头）：100 101 102
- 成功（2字头）：200 201 202 ...
- 重定向（3字头）：300 301 302 ...
- 请求错误（4字头）：400 401 402 ...
- 服务器是错误（5字头）：500 501 502 ...
- [参考](http://tool.oschina.net/commons?type=5)

### 常用端口

- HTTP:`80` 8000 8080
- HTTPS:443
- FTP:21
- SMTP:25
- SSH:22
- ...
- [参考](http://tool.oschina.net/commons?type=7)

## Task 1 发送HTTP请求

Python中有三个常用的库可以用来发送HTTP请求，分别是`urllib` `urllib2` `httplib`，详细用法可以查询官方文档
Python比较好用的第三方库还有`pycurl`和`requests` 可以通过pip进行安装
使用Python发送GET请求只需要使用下面的几行代码
```python
#-*-coding:utf-8-*-
import urllib2
url = "http://www.love-sysu.com/cloud"
res = urllib2.urlopen(url)
print res.read()
```
上面代码就实现了，用程序向指定url发送GET请求，然后将获得的html代码打印出来

```python
#-*-coding:utf-8-*-
import urllib, urllib2
url = "http://www.love-sysu.com/cloud"
data = {
    "name":"曾兆阳",
    "id":"12353255"
}
para = urllib.urlencode(data)
res = urllib2.urlopen(url+'?'+para)
print res.read()

#url = "http://www.love-sysu.com/cloud?name=zengzhaoyang&id=12353255"
#res = urllib2.urlopen(url)
#print res.read()

#如果大家在windows的cmd下面运行程序，姓名和学号都正确而我返回parameters error的话，那是因为cmd下的中文编码是gbk，而我服务端程序用的是utf-8编码，这时候大家只需要把data改成这样
#data = {
#   "name":"曾兆阳".decode("gbk").encode("utf-8")
#   "id":"12353255"
#}
#通过这样改变中文字符的编码应该就可以正常运行了，下面的post的程序也可以用同样的方法修改
```
上面代码是GET请求添加参数的实现

```python
#-*-coding:utf-8-*-
import urllib, urllib2
url = "http://www.love-sysu.com/cloud"
data = {
    "name":"曾兆阳",
    "id":"12353255",
    "email":"664587718@qq.com",
    "random_code":"754943"
}
para = urllib.urlencode(data)
req = urllib2.Request(url, para)
res = urllib2.urlopen(req)
print res.read()
```
上面代码是POST请求添加参数的实现

#### 任务要求：通过向  http://www.love-sysu.com/cloud  发送get请求，携带姓名和学号的参数，获得一个random_code，然后将学号、姓名、邮箱以及random_code作为参数post往同个url

## Task 2 处理HTTP请求

Python搭建最简单的服务器程序只需要下面一行的指令
```bash
python -m SimpleHTTPServer
```
上面指令就在本机开启了一个服务器，监听所有ip，监听本机8000端口，然后在本地浏览器访问 http://localhost:8000 或者在同个网段上的电脑打开浏览器访问 http://yourip:8000，就可以访问本地的文件了。
这个指令可以用来在电脑之间互传文件，还是比较方便的

```python
import web
urls = (
    '/', 'hello'
)
app = web.application(urls, globals())
class hello:        
    def GET(self):
        print web.input()
        return "GET hello world"
    def POST(self):
        print web.input()
        return "POST hello world"
if __name__ == '__main__':
    app.run()
#web.py的默认监听地址为 0.0.0.0：8080
#你可以通过 python <name>.py <host> <port>的方式来指定监听的ip或端口
#比如 python server.py 127.0.0.1
#    python server.py 80
#    python server.py 127.0.0.1:80
```
上面的程序是新建了一个简单的web.py框架的服务器，主要关注urls和class部分。urls是将发送到某个虚拟路径的请求交给某个类来处理，上面的例子就是将发送到虚拟路径'/'的请求交给类hello来处理。在hello中，定义了GET和POST两种请求的处理方式，web.input()是讲请求中的参数给提取出来，并且已经整理成了非常漂亮的字典的形式，return即为要返回的字符串，可以是任意字符串，当然也可以是html的代码

#### 任务要求：在本机搭建一个简单的http服务器，然后通过前面的get请求和post请求的代码，向自己的服务器发送请求并成功返回
