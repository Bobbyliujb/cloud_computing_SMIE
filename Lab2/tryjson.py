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