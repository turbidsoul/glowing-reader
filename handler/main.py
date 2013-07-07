# -*- coding: utf8 -*-


from handler import BaseHandler


class MainHandler(BaseHandler):
    """主页"""
    def get(self):
        self.render('main.html')


class LoginHandler(BaseHandler):
    """
    登录
    """
    def get(self):
        self.render('login.html')

    def post(self):
        self.redirect('/')
