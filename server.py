# -*- coding: utf8 -*-


import tornado.ioloop
import tornado.web
from handler.reader import ReaderHandler
import settings


application = tornado.web.Application([
    (r'/reader', ReaderHandler)
], debug=settings.debug)


if __name__ == '__main__':
    application.listen(8888)
    print('127.0.0.1:8888')
    tornado.ioloop.IOLoop.instance().start()
