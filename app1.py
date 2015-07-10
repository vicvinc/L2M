from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application, url
# from tornado.web import Httpserver

class HelloHandler(RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return Application([
        url(r"/", HelloHandler),
        ])

def main():
    app = make_app()
    server = HTTPServer(app)
    server.bind(8888)
    server.start(0)  # forks one process per cpu
    IOLoop.current().start()
if __name__ == '__main__':
    main()