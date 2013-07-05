# -*- coding: utf8 -*-

from handler import BaseHandler


class ReaderHandler(BaseHandler):
    def get(self):
        self.render('reader.html')
