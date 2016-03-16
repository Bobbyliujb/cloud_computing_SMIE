# 实验三

## 表单

表单在网页中主要负责数据采集功能。一个表单有三个基本组成部分： 表单标签：这里面包含了处理表单数据所用CGI程序的URL以及数据提交到服务器的方法。 表单域：包含了文本框、密码框、隐藏域、多行文本框、复选框、单选框、下拉选择框和文件上传框等。 表单按钮：包括提交按钮、复位按钮和一般按钮；用于将数据传送到服务器上的CGI脚本或者取消输入，还可以用表单按钮来控制其他定义了处理脚本的处理工作。

### HTML中的表单

在浏览器中，从地址栏输入一个url然后打开，这样发送的是一个GET请求，若要使用浏览器来发送POST请求，就需要使用表单了。（当然牛的可以用javascript来发送请求）

HTML中的表单是由form标签来声明的，下面是一个简单的form的例子
```html
<form action="login" method="post">
	<label>username:</label>
	<input type="text" name="username"><br />
	<label>password:</label>
	<input type="password" name="password"><br />
	<input type="submit" name="submit">
<form>
```
上面代码中，由form标签包含的部分便是表单的内容，其中关注其中的input部分，这个表单中有三个input，一个是text类型的，代表普通的文本输入，一个是password类型的，代表密码输入，一个是submit类型的，是一个提交的按钮；form标签定义了两个属性，一个是action，代表这个表单提交的路径，一个是method，代表这个表单提交的方法，缺省为GET。

当用户点下submit的按钮的时候，这时候浏览器就向action的路径发送了一个POST请求，请求的内容是下面这个样子的
```python
data = {
	'username':'XXXXXXXX',
	'password':'XXXXXXXX'
}
```
就是将各个除了submit之外的input的name作为key值，实际填写的数据作为value值作为数据包，发送了一个POST请求，当然，如果吧method改为get的话，那么发送的就是GET请求了

接下来，服务器所接收到的的请求数据就跟从客户端程序那边发过来的数据是一样的了，接下来就是根据发送过来的数据，做对应的处理然后返回了

## Task 1 实现简单的注册登录系统

#### 任务要求：实现一个简单的注册登录系统，有注册功能和登录功能，注册后服务器将注册信息储存到本地，登录时验证登录信息是否正确

网页方面可以参考上面表单的实现方式，只需要实现简单的功能即可，用户体验、美观方面不做要求

Python的web.py在返回网页的方面也提供了非常好的支持，主要使用其自带的template功能
```python
#-*-coding:utf-8-*-
import web
import os

urls = (
    '/', 'hello',
    '/login', 'login',
    '/regist', 'regist'
)
app = web.application(urls, globals())
class hello:
    def __init__(self):
        self.render = web.template.render('templates/')
    def GET(self):
        return self.render.form()


class login:
    def POST(self):
        para = web.input()
        username = para['username']
        password = para['password']

        #TODO:...
        #if authenticate(username,password):
            #return render.hello(username)
        return 'hello world'

class regist:
    def GET(self):
        return 'hello world'
        #return self.render.form()
    def POST(self):
        para = web.input()
        username = para['username']
        password = para['password']

        #TODO:...
        return 'hello world'

if __name__ == '__main__':
    app.run()
```

## Task 2 使用聚合数据网的API（选做）

任务要求：使用[聚合数据api](http://www.juhe.cn/)，查看相关文档，发送GET请求或POST请求，自己挑选一些功能实现

## Task 3 使用新浪微博API（选做）

任务要求：（较难）使用[新浪微博api](http://open.weibo.com/)，调用微博api接口，实现微博发送，读取等功能

新浪微博给Python提供了第三方强大的SDK，可以通过pip进行安装
```bash
sudo pip install sinaweibopy
```

下面代码实现了简单的使用程序发送微博的功能
```python
#-*-coding:utf-8-*-
import weibo  #导入weibo的库

APP_KEY = 'XXXXXXXXXX'
APP_SECRET = 'XXXXXXXXX'
CALL_BACK = 'XXXXXXXXX'
#上面三个变量是在微博开放平台上创建应用时反馈回来的值

client = weibo.APIClient(APP_KEY, APP_SECRET, CALL_BACK)  #新建新浪微博客户端
auth_url = client.get_authorize_url()
print auth_url  
#打印授权url，这时将该url复制到浏览器，授权之后，在回调页的url中获得code值，将code值作为下面的输入

code = raw_input()
r  = client.request_access_token(code)
client.set_access_token(r.access_token, r.expires_in)
client.statuses.update.post(status="这条是测试用的微博")
#到官方文档查看api的使用方法，替换掉上面的statuses update post以及参数即可调用其他的api接口
```
