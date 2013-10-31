# -*- coding: utf8 -*-


import feedparser


def get_feed(url):
    return feedparser.parse(url, request_headers={'Cache-control': 'max-age=0'})
