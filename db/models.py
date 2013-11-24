# -*- coding: utf8 -*-

from db import Base, query_filter_append
from datetime import datetime
from sqlalchemy import Column, String, Sequence, Integer, DateTime, Boolean, Text


class Feed(Base):
    """Feed Model"""
    __tablename__ = 'feed'
    feed_id = Column(Integer, Sequence('feed_id_seq'), primary_key=True, index=True)
    feed_title = Column(String, nullable=False, index=True)
    feed_url = Column(String(255), nullable=False, index=True)
    feed_link = Column(Text, nullable=False, index=True)
    last_load_time = Column(DateTime, index=True)
    create_time = Column(DateTime, default=datetime.now(), index=True)

    def feed_items(self, session, columns=None, offset=None, limit=None, lock_mode=None, order_by=None, **kwargs):
        query = session.query(FeedItem)
        query_filter_append(query, columns, offset, limit, lock_mode, order_by)
        if kwargs:
            query.filter_by(**kwargs)
        return query.all()


class FeedItem(Base):
    """Feed Item Model"""
    __tablename__ = 'feed_item'
    item_id = Column(Integer, Sequence('feed_item_id_seq'), primary_key=True, index=True)
    feed_id = Column(Integer, index=True)
    item_title = Column(String(250), nullable=False, index=True)
    item_descrition = Column(Text, index=True)
    item_url = Column(String(255), nullable=False, index=True)
    content = Column(String, index=True)
    star = Column(Boolean, default=False, index=True)
    save = Column(Boolean, default=False, index=True)

    def news(self, session, columns=None, limit=None):
        query = session.query(FeedItem)
        query_filter_append(query, columns=columns, limit=limit)
        return query.all()

class Tag(Base):
    """Tag Model"""
    __tablename__ = 'tag'
    tag_id = Column(Integer, Sequence('tag_id_seq'), primary_key=True, index=True)
    tag_name = Column(String(50), index=True)
    count = Column(Integer, index=True)
