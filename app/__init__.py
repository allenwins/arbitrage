# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from flask_script import Manager, Command, Shell
from flask_migrate import Migrate, MigrateCommand

import os, config

# init app
app = Flask(__name__)
app.config.from_object('config')

# initializes extensions
db = SQLAlchemy(app)
mail = Mail()
mail.init_app(app)
migrate = Migrate(app, db)

# import views
from . import views
app.add_url_rule('/taoli/', view_func=views.TaoLi.as_view('show_taoli'))
app.add_url_rule('/subscribe/', methods=['POST'], view_func=views.Subscribe.as_view('subscribe'))
app.add_url_rule('/api/taoli/', view_func=views.ApiTaoLi.as_view('api_taoli'))
app.add_url_rule('/api/notifyall/', view_func=views.NotifyAll.as_view('api_notifyall'))
