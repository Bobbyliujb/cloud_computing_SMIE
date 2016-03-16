# 实验四

### WSGI

Web服务器网关接口（Python Web Server Gateway Interface，缩写为WSGI)是Python应用程序或框架和Web服务器之间的一种接口，已经被广泛接受, 它已基本达成它的可移植性方面的目标。

在SAE中也是使用WSGI来进行HTTP请求与Web服务器之间的衔接，在SAE上创建一个Python应用之后，对url发送的HTTP请求将会由一个index.wsgi的文件来进行处理。WSGI的语法与Python的语法完全一致。使用WSGI的时候，只需要在原有代码的基础上加上几行代码即可。

若自己本地部署的服务器（如Apache，Nginx等）要使用到Python脚本来处理Web请求，同样也需要用到WSGI，在Web服务器的配置文件中配置好虚拟路径的映射以及使用的脚本即可。（这个主要应用在虚拟机服务器上，SAE是云应用引擎所以不需要用到这个）

## Task 1 创建SAE应用

#### 任务要求：注册SAE账号，创建第一个Python应用，实现Hello World程序

新浪SAE的地址为[http://sae.sina.com.cn](http://sae.sina.com.cn)，用微博账号即可登录注册
创建应用之后，使用svn工具即可创建一个空的代码版本，在本地编辑完代码之后可以直接进行提交（当然新浪也提供了在线编辑的窗口，本地编辑完之后进行复制粘贴即可）

一个最简单的SAE应用又两部分组成，一个是index.wsgi，一个是config.yaml

下面是一个Hello World的范例

- index.wsgi

```python
#-*-coding:utf-8-*-
import sae
import web

urls = (
	'/','hello'
)

class hello:
	def GET(self):
		return "hello"

app = web.application(urls,globals()).wsgifunc()
application = sae.create_wsgi_app(app)

```

- config.yaml

```bash
name: zengzhaoyang
version: 1

libraries:
- name: webpy 
  version: "0.36"
  
...

```

通过上面两个文件即可创建了一个Hello World级别的SAE应用。其中index.wsgi的作用跟之前在本地搭建服务器的server.py的作用是一样的，基本的语法结构除了最后app.run()的部分有所差别之外，其他部分是基本一样的，因此在本地可以先使用app.run()进行测试，要上传的时候再修改即可。config.yaml是第三方库使用的配置文件，SAE支持一定的python的第三方库，若要使用的时候需要同时在config.yaml中指定，web.py属于第三方库，因此需要指定。

在SAE的应用中一般还需要两个文件夹，一个是“templates”文件夹，用来让web.py的render template功能使用，存放html文件，另个一个是“static”文件夹，用来存放图片、css、js等静态文件（注意，此文件夹只有被命名为static才能够被访问）。另外，在SAE上是不支持读取本地文件的，也就是如果在同个目录放置一个txt文件然后使用py文件来读取是不可行的，若要实现类似注册登录的功能，需使用数据库功能，SAE提供了数据库的服务，直接开通即可使用，在Python中也有相应的接口可以使用

## Task 2 云迁移

标题说得比较好听，实际上就是将自己之前试验的一些小程序迁移到SAE上面去运行，txt文件可以暂时直接以Python的字典格式进行存储，在SAE上是支持多个py文件之间相互import的