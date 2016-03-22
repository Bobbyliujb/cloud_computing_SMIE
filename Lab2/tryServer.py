#-*-coding:utf-8-*-
import urllib, urllib2
import json

url = "http://115.29.136.57:8080/"
name = raw_input("请输入姓名：")
data = {
    "name":name
}
para = urllib.urlencode(data)
res = urllib2.urlopen(url+'?'+para)
data = json.loads(res.read())
if data["stat"] == "error":
  print u"出错了！%s" % (data["msg"])
else:
  print u"姓名:%s 学号:%s 性别:%s" % (data["name"], data["id"], data["sex"])
