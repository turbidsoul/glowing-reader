# -*- coding: utf8 -*-

from db.models import Feed


f = Feed('Turbidsoul', 'http://blog.turbidsoul.me')
result = f.save()
print(result)
result = Feed.find_all()
print(result)