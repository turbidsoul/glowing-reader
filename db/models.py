# -*- coding: utf8 -*-

from db import Base, query_filter_append
from datetime import datetime
from sqlalchemy import Column, String, Sequence, Integer, DateTime, Boolean, text


class Feed(Base):
    """Feed Model"""
    __tablename__ = 'feed'
    feed_id = Column(Integer, Sequence('feed_id_seq'), primary_key=True)
    feed_title = Column(String, nullable=False)
    feed_url = Column(String(255), nullable=False)
    feed_link = Column(String(255), nullable=False)
    last_load_time = Column(DateTime)
    create_time = Column(DateTime, server_default=text('now()'))

    def feed_items(self, session, columns=None, offset=None, limit=None, lock_mode=None, order_by=None, **kwargs):
        query = session.query(FeedItem)
        query_filter_append(query, columns, offset, limit, lock_mode, order_by)
        if kwargs:
            query.filter_by(**kwargs)
        return query.all()


class FeedItem(Base):
    """Feed Item Model"""
    __tablename__ = 'feed_item'
    item_id = Column(Integer, Sequence('feed_item_id_seq'), primary_key=True)
    feed_id = Column(Integer)
    item_title = Column(String, nullable=False)
    item_descrition = Column(String)
    item_url = Column(String(255), nullable=False)
    content = Column(String)
    star = Column(Boolean, default=False)
    save = Column(Boolean, default=False)


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
