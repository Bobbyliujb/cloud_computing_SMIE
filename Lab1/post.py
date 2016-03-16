#-*-coding:utf-8-*-
import urllib, urllib2
url = "http://www.love-sysu.com/cloud"
data = {
    "name":"曾兆阳",
    "id":"12353255",
    "email":"664587718@qq.com",
    "random_code":"31023104"
}
para = urllib.urlencode(data)
req = urllib2.Request(url, para)
res = urllib2.urlopen(req)
print res.read()
