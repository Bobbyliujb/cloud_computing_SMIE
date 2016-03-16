# 近期问题汇总解答

### ubuntu虚拟机要怎么连，没有图形界面吗
答： 没有，ubuntu-server的系统是没有GUI的，windows系统下面可以通过putty远程连接，Linux/Mac系统可以通过ssh来连接。此外，别想说在ubuntu-server系统上装vncserver企图远程桌面，这样就算连过去也是一团黑的

### 怎么传文件到虚拟机上面
答： windows server系统上面直接开浏览器下载资源就行，本地要传上去的话发发QQ邮件之类的大家懂的；ubuntu-server系统上面，如果要从windows系统往虚拟机传东西的话，可以下载个winscp软件，体积也非常小，如果从Linux/Mac系统要往虚拟机传东西的话，可以使用scp指令，scp指令大概使用方法如下：
```bash
scp the/path/of/yourfile azureuser@XXX.cloudapp.net:your/target/path  #从本地上传到虚拟机
scp azureuser@XXX.cloudapp.net:your/target/file/path your/local/path  #从虚拟机传到本地
```

### 用web.py如何上传文件
答： 可以参考下面代码
```python
# python服务端
def POST(self):
    data = web.input(myfile = {})
    filename = data.myfile.filename
    filedata = data.myfile.file.read()
    # myfile是在html表单中input元素的"name"
    # filename是上传过来的文件的文件名，不同浏览器传过来的文件名可能路径不大一样，一般以"/"字符做分割，取最后一段即为文件名
    # filedata是读取到的文件信息，可以用 f = open(filename,"wb") 然后 f.write(filedata) 类似的语法写成本地文件

```
```html
<!--html网页端-->
<form method="post" action="/">
	<input type="file" name="myfile" id="myfile">
</form>
```

### web.py的template中的$符号与jQuery中的$冲突了怎么办
答： web.py模板中的$是没办法更改的，可以考虑将jQuery中的"$"全部替换成"jQuery"。如果觉得麻烦的话，可以考虑使用python的模板框架Jinja，详情可百度，这个模板框架是使用大括号来作变量标记实现替换的，与jQuery中的"$"不会冲突

### 本地电脑如何配置MySQLdb
答： ubuntu-server系统要配置MySQLdb可以输入下面的指令
```bash
sudo apt-get install python-dev
sudo apt-get install libmysqld-dev
sudo apt-get install libmysqlclient-dev
sudo apt-get install python-mysqldb
```

### 客户端与云平台如何实现交互
答： 客户端大概据了解的情况有三种，网页、安卓端、微信。
- 网页端大概过程是：浏览器发送http请求到服务器--->服务器返回html字符串--->浏览器渲染html
- 安卓端大概过程是：安卓端发送http请求到服务器--->服务器整合需要的数据成一个json字符串返回--->安卓端解析json字符串并做出相应的动作给永固看
- 微信端大概过程是：用户发送消息到微信服务器--->微信服务器发送相应xml格式数据到服务器--->服务器解析xml字符串--->服务器将要返回的数据整合成xml格式字符串返回给微信服务器--->微信服务器发送给用户
- 问题比较多的是安卓端的，这个其实设计要点就是在自己设计交互的api，建议先把需求写成简易的文档，然后封装成api，服务端和客户端再根据需求文档去实现成代码，不然想到什么写什么是比较混乱的。建议大家可以去搜一下**Restful API**，这是一种当前广泛使用的API设计理念，设计起来比较方便

### 客户端如何访问数据库
答： 客户端不需要直接访问mysql数据库，可以通过云服务器做一个中介，客户端发送一个请求，携带一定的参数到服务器，服务器从数据库中获取数据之后再返回给客户端就可以。最差的方法其实，直接把整个sql语句当做参数发给服务器，服务器直接拿这个sql语句去查询也是可以的，就是比较挫而已

