# 云计算实验指导

## 教学资料
- [项目报告模板](ftp://smie@211.66.129.33/%D4%C6%BC%C6%CB%E3%D3%A6%D3%C3%D1%D0%BE%BF%CF%EE%C4%BF%CA%E9%C4%A3%B0%E6.doc)
- [相关研究论文](ftp://smie@211.66.129.33/IEEECS_CPS_LaTeX_Letter_2Col.zip)
- [作业模板_Cloud_Application](ftp://smie@211.66.129.33/%D7%F7%D2%B5%C4%A3%B0%E5_Cloud_Application.pdf)
- [云计算组队情况](ftp://smie@211.66.129.33/%D4%C6%BC%C6%CB%E3%D7%E9%B6%D3%C7%E9%BF%F6%A3%A8%BC%D3%CB%E6%BB%FA%B7%D6%C5%E4%A3%A9.xlsx)
- [Chapter 0课件](ftp://smie@211.66.129.33/Chapter%200%20Introduction.pdf)
- [Chapter 1课件](ftp://smie@211.66.129.33/Chapter%201%20Cloud%20Computing%20Basics.pdf)

## 课程动态
- **Project Proposal提交地址为 [这里](http://211.66.129.33:8080) 截止时间为10月20日23:59**
- Project Proposal 提交时间推迟到10月20日
- Cloud Application作业的提交地址为 [这里](http://211.66.129.33:8080) 截止时间为10月10日23:59
- 10月10日前需完成Cluod Application作业，每个人需提交一份，提交方式另行公布
- 10月15日前需提交Project Proposal，每个组需提交一份，提交方式另行公布

## 学期时间安排
- 1-3周 熟悉http请求，学会使用程序发送http请求，以及编写简单的server端程序，处理http请求
- 4-5周 熟悉`新浪sae`云平台的使用
- 6-7周 熟悉`微软windows azure`云平台的使用
- 8周起  以`project`或者`research`为向导，小组进行自主开发

## 教学语言

server端和client端的程序对语言没有限制，有基础的同学可以自行选择语言进行开发，考虑到`新浪sae`云平台只支持 Java Python Php，所以建议选择这三种语言。对于没有基础的同学，考虑到先前实训已经对Python语言有了一定的入门了解，所以教学语言将使用Python，服务器框架将使用Python的web.py框架，这个是一个比较简单轻量级的web框架。有兴趣的同学可以自己了解使用一下Python的其他框架，有 django flask tornado，详情参见百度

## 环境配置

实验过程建议在ubuntu系统下进行，环境需要配置python2.7，ubuntu系统已经自带
通过下面指令可以完成ubuntu系统下的环境配置
```bash
sudo apt-get install python-dev  #这条语句仅用于系统下没有python的时候
sudo apt-get install python-pip  #这条语句用于安装python的第三方库安装包pip
sudo pip install web.py  #这条语句用于配置python的第三方库web.py
sudo apt-get install git  #本次实验中需要用到git版本控制工具
sudo apt-get install subversion  #sae的使用需要用到svn
sudo apt-get install texlive  #安装latex
```

windows下面安装pip可以通过下面方式来下载
[pip](https://bitbucket.org/pypa/setuptools/get/default.tar.gz#egg=setuptools-dev)
```bash
#运行下面指令之前先把python的安装路径添加到系统的环境变量中
#通过上面链接可以下载pip到本地，然后解压，在解压后的目录执行
python setup.py install
#然后就可以通过下面指令来安装web.py了
python easy_install.py web.py
```


使用pip可以安装绝大部分的python第三方库
安装完后，在python命令行模式下，输入
```python
import web
```
若没有报错，则是安装成功

第一次实验可以通过下面语句将本工程文件克隆到本地
```bash
git config -—global user.email "13631252971@163.com"
git config —-global user.name "guest"
git clone http://182.92.104.30:5000/zzy/cloud_computing.git
```
克隆下目录之后，最好不要在克隆得到的目录里面修改文件，不然之后会有文件冲突的干扰，最好新建个文件夹复制过去再进行修改。对git的操作比较熟练的同学也可自行搞定
以后每次实验有更新的话，只需要在第一次克隆得到的目录下面执行下面语句即可
```bash
git pull
#如果报错的话可以执行以下下面语句
git stash
```
git的版本控制可以参考书籍《Pro git》

## 实验要求

- `新浪sae`的使用是要求每个人独立完成，使用微博账号可到新浪sae上注册
- `微软windows azure`的使用是三个人一组，自由组队，到时候会发放azure的账号
- 第三周前组好自己的队伍，在第四周时需上交大project的项目进度计划书
- 大project需要按照工程型的标准来完成，期末需要提交项目文档、测试文档等
- 大project的项目文档、research的论文报告需要使用latex进行编写

## 参考资料
- [python文档](https://docs.python.org/2/library/index.html)
- [web.py文档](http://webpy.org/)
- [sae文档](http://sae.sina.com.cn/doc/)
- [windows和mac下安装pip](https://pypi.python.org/pypi/setuptools/)
- [git安装与文档](http://git-scm.com/)
- [svn安装与文档](http://tortoisesvn.net/)
- [latex入门教程](http://www.360doc.com/content/13/0117/11/2886802_260681908.shtml)
