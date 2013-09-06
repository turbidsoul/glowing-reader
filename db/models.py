# -*- coding: utf8 -*-

from db import Model
from sqlalchemy import Column, String, Sequence, Integer


class Feed(Model):
    """Feed Model"""
    __tablename__ = 'feed'
    id = Column(Integer, Sequence('feed_id_seq'), primary_key=True)
    title = Column(String)
    link = Column(String(255))

    def __init__(self, title, link):
        self.title = title
        self.link = link


class User(Model):
    """User Model"""
    pass


class Tag(Model):
    """Tag Model"""
    pass
