#-*-coding:utf-8-*-
import urllib, urllib2
url = "http://www.love-sysu.com/cloud"
data = {
    "name":"曾兆阳",
    "id":"12353255"
}
para = urllib.urlencode(data)
res = urllib2.urlopen(url+'?'+para)
print res.read()

#url = "http://www.love-sysu.com/cloud?name=zengzhaoyang&id=12353255"
#res = urllib2.urlopen(url)
#print res.read()
