#-*-coding:utf-8-*-
import re  #python中使用正则表达式需导入此库
import urllib2

url = "http://www.hao123.com"
res = urllib2.urlopen(url)
data = res.read()
#上面获取了hao123网页的网页源代码

href = 'href="(.*?)"'  #定义正则表达式的句法规则
href_re = re.compile(href)  #通过compile函数“编译”正则表达式
href_info = href_re.findall(data)  #通过findall函数，查找整个网页源代码的所有内容，返回的是所有匹配字符串组成的列表

for item in href_info:
    print item