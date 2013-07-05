# -*- coding: utf8 -*-

import os
from jinja2 import Environment, FileSystemLoader

base_path = os.path.split(os.path.realpath(__file__))[0]

template_path = os.path.join(base_path, "template")
db_file = os.path.join(base_path, 'db.sqlite')

debug = True


jinja2_env = Environment(loader=FileSystemLoader(template_path), auto_reload=debug)
