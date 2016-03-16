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