#!/usr/bin/env python
# -*- coding: utf-8 -*-

from werkzeug.middleware.proxy_fix import ProxyFix
from wsgiref.simple_server import make_server
from app import app


app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1)

httpd = make_server('localhost', 8000, app)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请示
httpd.serve_forever()
