# -*- coding: utf8 -*-

from db import Base
from sqlalchemy import Column, Integer, String, Sequence


class Feed(Base):
    """Feed Model"""
    __tablename__ = "feed"

    id = Column(Integer, Sequence('feed_id_seq'), primary_key=True)
    title = Column(String(255))
    link = Column(String(255))

    def __init__(self, title, link):
        self.title = title
        self.link = link


class User(Base):
    """User Model"""
    pass


class Tag(Base):
	"""Tag Model"""
	pass
