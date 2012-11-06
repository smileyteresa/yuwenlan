# -*- coding: utf-8 -*-

from flask import Flask
from views import blue
from config import Mysql_Uri
from database import db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Mysql_Uri
app.secret_key = "development key"
#初始化数据库
db.init_app(app)
db.app = app

for key, value in blue.items():
    if key == 'welcome':
        app.register_blueprint(value)
    else:
        app.register_blueprint(value, url_prefix = "/" + key)

if __name__ == '__main__':
    app.run(debug = True)