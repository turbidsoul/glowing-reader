# -*- coding: utf8 -*-

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

_engine = create_engine("sqlite:///:memory:", echo=True)

def init_db():
    Base.metadata.create_all(_engine)

def drop_db():
    Base.metadata.drop_all(_engine)

def query_filter_append(query, columns=None, offset=None, limit=None, lock_mode=None, order_by=None):
    if columns:
        query.values(columns)
    if offset:
        query.offset(offset)
    if limit:
        query.limit(limit)
    if order_by:
        query.order_by(*order_by)
    if lock_mode:
        query.with_lockmode(lock_mode)
    return query


class Model(object):

    def save(self, session):
        session.add(self)
        session.commit()
        return self

    def update(self, session):
        session.update(self)
        session.commit()
        return self;

    @classmethod
    def find_all(cls, session, columns=None, offset=None, limit=None,
                 order_by=None, lock_mode=None):
        query = session.query(cls)
        query_filter_append(query, columns, offset, limit, lock_mode, order_by)
        return session.all()

    @classmethod
    def find(cls, session, columns=None, offset=None, limit=None, order_by=None,
             lock_mode=None, **kwargs):
        query = session.query(cls)
        query_filter_append(query, columns, offset, limit, lock_mode, order_by)
        if kwargs:
            query.filter_by(**kwargs)
        return query.all()

    @classmethod
    def count(cls, session, lock_mode=None, **kwargs):
        query = session.query(cls)
        if kwargs:
            query.filter_by(**kwargs)
        if lock_mode:
            query.with_lockmode(lock_mode)
        return query.count()

    @classmethod
    def exists(cls, session, lock_mode=None, **kwargs):
        query = session.query(cls)
        if kwargs:
            query.filter_by(**kwargs)
        if lock_mode:
            query.with_lockmode(lock_mode)
        return session.query(query.exists()).scalar()



Base = declarative_base(cls=Model)
Session = sessionmaker(bind=_engine)
