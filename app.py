import config.settings

from flask import Flask
from flask_caching import Cache

import logging
import logging.config

from apps.book.models import db
from apps.book.views.book import book

app = Flask(__name__)

logging.config.fileConfig('logging.conf')

redisConfig = {
    'CACHE_TYPE': 'RedisCache',       #使用redis作为缓存
    'CACHE_REDIS_HOST': '127.0.0.1',     #redis地址
    'CACHE_REDIS_PORT': 6379,     #redis端口号
    'CACHE_REDIS_DB': '1'
}
cache = Cache()
cache.init_app(app=app, config=redisConfig)


def create_app():

    logging.info("[App is starting...]")

    # 装载配置
    app.debug = config.settings.DEBUG
    app.config.update(config.settings.settings)
    # 数据库
    db.app = app
    db.init_app(app)

    cache.set("test", "test")

    # db.drop_all()
    # 打开之后可以重新建表
    # db.create_all()

    app.register_blueprint(book, url_prefix='/book')

    return app

@app.route('/test')
def test():

    testVal = cache.get("test");
    logging.info("testVal====" + testVal)

    return testVal

if __name__ == '__main__':
    create_app().run()

