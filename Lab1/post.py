#-*-coding:utf-8-*-
import urllib, urllib2
url = "http://0.0.0.0:8080/"
data = {
    "name":"bobo",
    "id":"123",
    "email":"123@qq.com",
    "random_code":"31415926"
}
para = urllib.urlencode(data)
req = urllib2.Request(url, para)
res = urllib2.urlopen(req)
print res.read()
