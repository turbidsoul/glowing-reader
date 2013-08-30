# -*- coding: utf8 -*-

import os
from jinja2 import Environment, FileSystemLoader

base_path = os.path.split(os.path.realpath(__file__))[0]

title = "Glowing Reader"
wwwroot = "http://127.0.0.1:8888"
template_path = os.path.join(base_path, "template")
db_file = os.path.join(base_path, 'db.sqlite')
static_path = os.path.join(base_path, 'static')

debug = True

jinja2_env = Environment(loader=FileSystemLoader(template_path), auto_reload=debug)

