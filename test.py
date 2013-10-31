# -*- coding: utf8 -*-

from db import Session, init_db, drop_db
from db.models import Feed
from nose.tools import assert_equal
from datetime import datetime

def setup():
    init_db()

def teardown():
    drop_db()

def test_feed_add_and_update():
    session = Session()
    feed = Feed("Turbidsoul's 的小黑屋", "http://blog.turbidsoul.me/rss.xml")
    feed.save(session)
    assert_equal(feed.feed_id, 1)
    feed.url = 'http://blog.turbidsoul.me'
    ltime = datetime.now();
    feed.last_update_time = ltime
    feed.update()
    Feed.find()


# session = Session()
# feed = Feed("Turbidsoul's 的小黑屋", 'http://blog.turbidsoul.me/rss.xml')
# feed.save(session)
# print(Feed.find_all(session))
# print(Feed.count(session))
# print(Feed.count(session, feed_id=1))
# print(Feed.exists(session))
# print(Feed.exists(session, feed_id=1))
