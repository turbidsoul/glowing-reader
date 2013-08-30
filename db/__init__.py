# -*- coding: utf8 -*-


import sqlite3
import settings

conn = sqlite3.connect(settings.db_file)
print(conn)
