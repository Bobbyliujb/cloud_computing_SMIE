#-*-coding:utf-8-*-
import urllib2
import json
import city  #这个文件在本工程里面已经给出，需要下载到本地


url = 'http://www.weather.com.cn/data/cityinfo/%s.html'
#url = 'http://m.weather.com.cn/data/%s.html'
#天气网API使用的是城市编码，城市编码在city.py文件中已经给出，上面的url的%s部分就是需要填充的城市编码部分
#范例 url = 'http://www.weather.com.cn/data/cityinfo/101010100.html'

city_name = raw_input("请输入城市名：")
if not city_name in city.citycode:
    print "城市名不存在"
    exit()

code = city.citycode[city_name]  #通过字典的key获得value

res = urllib2.urlopen(url%code)
a = res.read()
data = json.loads(a)
print u"%s,%s,%s 到%s ." % (data["weatherinfo"]["city"], data["weatherinfo"]["weather"], data["weatherinfo"]["temp2"], data["weatherinfo"]["temp1"])  # 在前面加u强制以unicode输出中文而不是ascii

#有兴趣的同学可以使用下面这个url然后进行解析
#url = 'http://m.weather.com.cn/data/%s.html'
#有兴趣的同学还可以去看看百度地图api，那个的json字符串更加具体明了有挑战性
