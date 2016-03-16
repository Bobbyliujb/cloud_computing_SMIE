# 实验七

### Task 1 在Linux机器上搭建LAMP服务器架构

LAMP服务器架构指的是 Linux+Apache+MySQL(Mongodb)+Php(Python) 框架的服务器架构，在这个架构中“L”作为操作系统，“A”作为WEB服务器，“M”作为数据库，“P”作为请求的执行脚本，实现功能的模块化分离。

在我们的实验中，使用的是 Linux+Apache+MySQL+Python

#### 环境配置

服务器的操作系统推荐使用CentOS或者Ubuntu server（CentOS系统比较稳定，但操作较难，这里使用的是Ubuntu server系统）
在Ubuntu系统下，可以用下面指令进行环境的配置
```bash
sudo apt-get install apache2 #安装apache服务器
sudo apt-get install libapache2-mod-wsgi #安装apache服务器的wsgi链接模块
sudo apt-get install mysql #安装mysql
```

接下来是配置让Apache驱动Python脚本

首先，假设我某个工作目录下面新建了这样一个script.wsgi文件
```python
import web
urls = (
    '/', 'hello'
)
app = web.application(urls, globals())
application = app.wsgifunc() #加上这一句即可
class hello:        
    def GET(self):
        return "hello world"
if __name__ == '__main__':
    app.run()

```

接下来需要修改Apache的配置文件，默认位置位于 /etc/apache2/sites-enabled/000-default
在配置文件中加入下面的语句
```conf
WSGIScriptReloading On #开启wsgi的reload模式，修改wsgi文件之后可以自动加载
WSGIScriptAlias /yourname "/your/path/script.wsgi" #定义虚拟路径和执行的脚本文件
<Directory "/your/path">
    Order Deny,Allow
    Allow from all #这句适用于Apache2.2，如果是Apache2.4的用这句 “Require all granted”
</Directory>
```

接下来重启一下Apache服务器
```bash
sudo service apache2 restart
```
然后访问一下  http://yourhost/yourname  这样就可以通过你的脚本来处理请求了

#### 注意事项

- Apache所属的用户组是www-data，如果涉及到一些要操作本地文件的有权限问题的，可以考虑将目标文件或者文件夹用chown修改一下用户组
- wsgi文件的reload只支持本身的reload，如果import了其他py文件，需要将Apache服务器重启
- 可以考虑搭建svn或者git服务器用以上传代码，这样就不用每次远程到虚拟机上面写代码了，百度一下有很多教程，然后设置一下hook中的post-commit事件，让每次代码提交之后自动update，这样就可以在自己电脑上写代码，每次提交即可，Apache会部署最新提交的代码
- 学会查看Apache的错误日志可以排查一些错误，日志位于 /var/log/apache2/error.log，一般用vim打开之后直接按“G”调到文件末尾就可以看到
