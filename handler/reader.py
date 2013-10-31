# -*- coding: utf8 -*-

from handler import BaseHandler
from feed import get_feed


class ReaderHandler(BaseHandler):
    def get(self, url=None):
        d = get_feed("http://blog.turbidsoul.me/rss.xml")
        return self.render('reader.html', feed=d.feed, entries=d.entries, page='reader')


class AddRssHandler(BaseHandler):
    def post(self, url, tag=None):
        pass
