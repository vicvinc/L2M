# import tornado.ioloop
# import tornado.web
from tornado.web import Application,RequestHandler
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
import tornado.template

class MainHandler(RequestHandler):
	# def __init__(self):
	# 	this = self
	def get(self):
		this = self
		this.write('this is this')
		this.write('   ->')
		this.write(repr(this))
		self.write('Hello, world')
class HomeHandler(RequestHandler):
	"""docstring for HomeHandler"""

	def get(self):
		self.write('this is homepage')
		loader = template.Loader("/home/btaylor")
		print loader.load("test.html").generate(myvalue="XXX")

class UserHandler(RequestHandler):
	"""docstring for HomeHandler"""

	def get(self):
		self.write('here is user profile')
if __name__ == '__main__':
	app = Application([
		(r'/', MainHandler),
		(r'/home', HomeHandler),
		(r'/index',HomeHandler),
		(r'/user',UserHandler)
	])
	sockets = tornado.netutil.bind_sockets(8888)
	#tornado.process.fork_processes(0)
	server = HTTPServer(app)
	server.add_sockets(sockets)
	IOLoop.current().start()