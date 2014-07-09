# -*- coding: utf8 -*-

import os
import traceback

import settings
from bottle import jinja2_template as template
from bottle import (abort, default_app, install, route, run, static_file,
                    TEMPLATE_PATH)
from bottle.ext import sqlite

TEMPLATE_PATH.insert(0, './template/')
install(sqlite.Plugin(dbfile='./db.sqlite'))


def renderer(f, **kwargs):
    params = {
        'title': settings.title
    }
    params.update(kwargs)
    return template(f, params)


@route('/static/<path:path>')
def staticfile(path):
    return static_file(path, settings.static_path);


@route('')
@route('/')
def index(db):
    cursor = db.execute("SELECT * FROM feed")
    feeds = cursor.fetchall()
    return renderer('index.html', feeds=feeds)




@route('/init')
def init(db):
    try:

        db.executescript('''CREATE TABLE IF NOT EXISTS "feed" (
            "id" INTEGER PRIMARY KEY autoincrement,
            "site_name" VARCHAR NOT NULL,
            "site_url" VARCHAR NOT NULL,
            "feed_url" VARCHAR NOT NULL,
            "last_update" DATETIME NOT NULL,
            "create_time" DATETIME NOT NULL
        );''')

        db.executescript('''CREATE TABLE IF NOT EXISTS "feed_item" (
            "id" INTEGER PRIMARY KEY autoincrement,
            "name" VARCHAR NOT NULL,
            "url" VARCHAR NOT NULL,
            "title" VARCHAR NOT NULL,
            "author" VARCHAR NOT NULL,
            "description" VARCHAR,
            "publish_date" DATETIME NOT NULL,
            "create_time" DATETIME NOT NULL
        );''')
        db.commit()
    except Exception:
        traceback.print_exc()
        abort(500, traceback.format_exc())
    return "初始化成功"


if __name__ == '__main__':
    run(host='127.0.0.1', port=9000, reloader=True, debug=True)
else:
    application = default_app()
