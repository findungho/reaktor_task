#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Module __init__.
# Description: Setup initial application and register Blueprints.
# Author : Dung Ho
# Email: fin.dungho@gmail.com


from flask import Flask
from config import Config
from application.controllers.views import html_view
from application.controllers.api import api_test


app = Flask(__name__)
app.config.from_object(Config)


def create_app():
    app = Flask(
        __name__,
        template_folder='templates',
        static_folder='static',
    )

    app.register_blueprint(html_view)
    app.register_blueprint(api_test)

    return app
