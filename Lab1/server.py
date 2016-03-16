import web
urls = (
    '/', 'hello'
)
app = web.application(urls, globals())
class hello:        
    def GET(self):
        print web.input()
        return "GET hello world"
    def POST(self):
        print web.input()
        return "POST hello world"
if __name__ == '__main__':
    app.run()