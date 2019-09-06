from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_debugtoolbar import DebugToolbarExtension
#当使用包组织代码时，为了确保其他扩展或测试框架获得正确的路径值
# 最好以硬编码的形式写出包名称作为程序名称，即sayhello
app = Flask('sayhello')
app.config.from_pyfile('settings.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.debug = True
toobar = DebugToolbarExtension(app)
from sayhello import views, errors, commands