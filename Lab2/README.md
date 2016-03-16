# 实验二

## Json数据交换格式

JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式。它基于JavaScript（Standard ECMA-262 3rd Edition - December 1999）的一个子集。 JSON采用完全独立于语言的文本格式，但是也使用了类似于C语言家族的习惯（包括C, C++, C#, Java, JavaScript, Perl, Python等）。这些特性使JSON成为理想的数据交换语言。易于人阅读和编写，同时也易于机器解析和生成

### Python中的字典

字典(dictionary)是Python中最灵活的内置数据结构类型，类似于C++中的map。与列表不同，列表是以偏移（下标）来实现存取的，而字典是以键值来实现存取的。字典与列表有相似之处，在Python中，都可以通过迭代的方式来进行遍历
下面是一个字典的例子
```python
data = {
    "name":"曾兆阳",
    "id":"12353255",
    "sex":"男",
    "age":20,
    "isSB":False,
    "girlfriend":["备胎1号","备胎2号","备胎3号"],
    "course":[
        {
            "subject":"高数",
            "score":100
        },
        {
            "subject":"线代",
            "score":100
        },
        {
            "subject":"软件设计",
            "score":100
        }
    ],
    "other":{
        "isFat":False,
        "isHandsome":True
    }
}
```
上面例子大概包括了字典类型的所有情况了，字典中的对象是无序的，每一个对象由一个键值对(key-value)构成，其中key为字符串，value可以为字符串、数字、列表或是另一个字典等

### Json格式字符串

Json格式的字符串，最直观的理解，可以认为是长得跟字典的形式一样的字符串，通过下面例子可以很直观地了解
```python
data = {
    "name":"zengzhaoyang",
    "id":"12353255"
}
# data是字典

data_json = '''{
    "name":"zengzhaoyang",
    "id":"12353255"
}'''
# data_json是一个字符串
```

通过上面例子，应该能比较清晰地理解Json格式的字符串

### 字典与Json字符串之间的转化

在Python中，提供了很强大的能实现Json字符串与字典之间进行转化的库，参考下面例子

```python
#-*-coding:utf-8-*-
import json  #将json库导入

data = {
    "name":"zengzhaoyang",
    "id":"12353255"
}
res1 = json.dumps(data)  #通过dumps函数可以将字典类型转化成字符串类型
print type(res1)
print res1

data_json = '''{
    "name":"zengzhaoyang",
    "id":"12353255"
}'''
res2 = json.loads(data_json)  #通过loads函数可以将字符串类型转化成字典类型
print type(res2)
print res2["name"],res2["id"]

```

## Task 1 调用天气网API，解析Json

#### 任务要求：上次实验中大家学会了使用urlopen来发送GET请求，这次将使用它来向天气网API的url发送GET请求，然后将返回的数据进行解析
```python
#-*-coding:utf-8-*-
import urllib2
import json
import city  #这个文件在本工程里面已经给出，需要下载到本地

url = 'http://www.weather.com.cn/data/cityinfo/%s.html'
#天气网API使用的是城市编码，城市编码在city.py文件中已经给出，上面的url的%s部分就是需要填充的城市编码部分
#范例 url = 'http://www.weather.com.cn/data/cityinfo/101010100.html'

city_name = raw_input("请输入城市名：")
if not city_name in city.citycode:
    print "城市名不存在"
    exit()

code = city.citycode[city_name]  #通过字典的key获得value

res = urllib2.urlopen(url%code)
data = json.loads(res.read())

# TODO:......

#有兴趣的同学可以使用下面这个url然后进行解析
#url = 'http://m.weather.com.cn/data/%s.html'
#有兴趣的同学还可以去看看百度地图api，那个的json字符串更加具体明了有挑战性
#百度地图api可参考http://developer.baidu.com/map/
```

## Task 2 服务器构造Json字符串并返回

#### 任务要求：上次实验中大家学会了使用web.py来搭建简单的服务器程序，处理GET请求和POST请求，这次实验在上次实验的基础上，实现下面功能
功能：客户端向服务端发送请求，请求携带的参数为名字，服务端程序接收到请求后，从本地txt文件读取与该名字相关的数据（比如学号，班级，性别，年龄等，txt可以自己构造），然后整合成Json格式的字符串返回，客户端接收到返回的字符串后进行解析打印
Python中文件读取操作可以使用下面语句来进行
```python
f = open("a.txt","r")
a = f.readline()
while a:
    print a
    a = f.readline()
#上面是按行读取文件，也可通过下面语句直接读取文件全部内容
# a = f.read()
```

下面是一个简单的读取txt文件之后提取信息以json格式返回的例子
```python
#-*-coding:utf-8-*-

##############################
# 假设a.txt文件内容像下面这样所示 #
# 张三 12345678 男            # 
# 李四 98765432 女            #
# 王五 87878787 男            #
##############################


import web
import json
urls = (
    '/', 'hello',
)
app = web.application(urls, globals())
class hello:        
    def GET(self):
        para = web.input()
        if not 'name' in para:
            res = {'stat':'error','msg':'parameters error'}
            return json.dumps(res)
        else:
            f = open('a.txt', 'r')
            data = dict()
            a = f.readline()
            while a:
                temp = a.split()
                print type(temp[0])
                if temp[0] == para['name'].encode('utf-8'):
                    data['name'] = temp[0]
                    data['id'] = temp[1]
                    data['sex'] = temp[2]
                    data['stat'] = 'ok'
                    return json.dumps(data)
                a = f.readline()
            f.close()
            data['stat'] = 'error'
            data['msg'] = 'The name does not exist'
            return json.dumps(data)

if __name__ == '__main__':
    app.run()
```

## Task 3 正则表达式（选做）

正则表达式使用单个字符串来描述、匹配一些列符合某个句法规则的字符串，下面是几个正则表达式的例子
```python
re1 = '<a href="(.*?)">'
#上面的字符串可匹配类似 <a href="XXXXXX"> 这种句法的字符串

re2 = 'aaa\d*bbb'
#上面的字符串可匹配以aaa开头，bbb结尾，中间是数字的字符串，类似 aaa13213121bbb
```
关于正则表达式的详细句法规则及使用方法，可以参考[这里](http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html)，这些规则不需要详细记住，能熟练常用的几个即可，需要用的时候可以查文档

正则表达式广泛使用与网络爬虫方面，下面例子是一个简单的网页爬虫的例子
```python
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
```
上面代码的作用就是将hao123网页中的所有链接提取出来并打印出来。如果通过广度优先搜索的方法，将获得的所有链接再进行urlopen，之后再将获得的网页中的链接给提取出来，这样就可以获得成千上网网页的内容了，然后在爬到的网页中提取一些有关的数据，就可以进行大数据的分析了