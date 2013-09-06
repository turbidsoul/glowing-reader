# -*- coding: utf8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


_engine = create_engine("sqlite:///:memory:", echo=True)
Base = declarative_base(bind=_engine)
_Session = sessionmaker()
_Session.configure(bind=_engine)
session = _Session()


class Model(Base):
    """Base Model"""

    def save(self):
        return session.add(self)

    @classmethod
    def find_all(cls):
        return session.query(cls).all()
