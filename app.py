# import tornado.ioloop
# import tornado.web
from tornado.web import Application,RequestHandler
from tornado.ioloop import IOLoop

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
	app.listen(8888)
	IOLoop.current().start()