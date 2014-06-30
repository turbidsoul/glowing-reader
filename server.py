# -*- coding: utf8 -*-

from bottle import default_app, jinja2_template as template, Bottle, TEMPLATE_PATH
from bottle.ext import sqlite

# import settings

TEMPLATE_PATH.insert(0, './template/')
app = Bottle()
app.install(sqlite.Plugin(dbfile=':memory:'))


def renderer(f, **kwargs):
    params = {
        'title': 'Fire Reader'
    }
    params.update(kwargs)
    return template(f, params)



@app.route('')
@app.route('/')
def index():
    return renderer('index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9000, reloader=True, debug=True)
else:
    application = default_app()
