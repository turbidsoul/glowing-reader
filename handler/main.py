# -*- coding: utf8 -*-


from handler import BaseHandler
from feed import get_feed


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


class SettingsHandler(BaseHandler):
    """设置"""
    def get(self):
        return self.render('settings.html', page='settings')


class AboutHandler(BaseHandler):
    """
    关于我
    """
    def get(self):     
        return self.render("about.html", page='about')


class ReaderHandler(BaseHandler):
    def get(self, url=None):
        d = get_feed("http://blog.turbidsoul.me/rss.xml")
        return self.render('reader.html', feed=d.feed, entries=d.entries, page='reader')


class AddRssHandler(BaseHandler):
    def post(self, url, tag=None):
        pass
