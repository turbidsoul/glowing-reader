# -*- coding: utf8 -*-

from db import Base
from datetime import datetime
from sqlalchemy import Column, String, Sequence, Integer, DateTime


class Feed(Base):
    """Feed Model"""
    __tablename__ = 'feed'
    feed_id = Column(Integer, Sequence('feed_id_seq'), primary_key=True)
    title = Column(String)
    url = Column(String(255))
    link = Column(String(255))
    last_update_time = Column(DateTime)
    create_time = Column(DateTime)


    def __init__(self, title, url, link):
        self.title = title
        self.url = url
        self.link = link
        self.create_time = datetime.now()



class User(Base):
    """User Model"""
    __tablename__ = 'user'
    user_id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    user_name = Column(String(50))
    password = Column(String)


class Tag(Base):
    """Tag Model"""
    __tablename__ = 'tag'
    tag_id = Column(Integer, Sequence('tag_id_seq'), primary_key=True)
    tag_name = Column(String(50))
    count = Column(Integer)
