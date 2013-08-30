# -*- coding: utf8 -*-


import feedparser


def get_feed(url):
    return feedparser.parse(url)
