import tornado.ioloop
import tornado.web
from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

    def post(self, *args, **kwargs):
        self.write("Post request")

class HostHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("show hosts")

class MapHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("show map")

class Application(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self, [
            (r"/host", HostHandler),
            (r"/map", MapHandler),
            (r"/", MainHandler),
                                         ])

def main():
    tornado.options.parse_command_line()
    Application().listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()