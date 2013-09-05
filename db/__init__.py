# -*- coding: utf8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import settings

engine = create_engine("sqlite:///%s" % settings.db_file, echo=True)
Base = declarative_base(bind=engine)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()