import config.settings

from flask import Flask

import logging
import logging.config

from apps.book.models import db
from apps.book.views.book import book

app = Flask(__name__)

logging.config.fileConfig('logging.conf')

def create_app():

    logging.info("[App is starting...]")

    # 装载配置
    app.debug = config.settings.DEBUG
    app.config.update(config.settings.settings)
    # 数据库
    db.app = app
    db.init_app(app)

    # db.drop_all()
    # 打开之后可以重新建表
    # db.create_all()

    app.register_blueprint(book, url_prefix='/book')

    return app


if __name__ == '__main__':
    create_app().run()

