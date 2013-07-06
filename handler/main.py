# -*- coding: utf8 -*-


from handler import BaseHandler


class MainHandler(BaseHandler):
    """主页"""
    def get(self):
        self.render('main.html')
