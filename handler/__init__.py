# -*- coding: utf8 -*-


from tornado.web import RequestHandler
from settings import jinja2_env


class BaseHandler(RequestHandler):
    """
    rewrite render_string
    """

    def render_string(self, template_name, **kwargs):
        template = jinja2_env.get_template(template_name)
        self.write(template.render(**kwargs))
