# -*- coding: utf8 -*-

import sqlite3



conn = sqlite3.connect("test.db")

cur = conn.cursor()

cur.execute('select * from test')
