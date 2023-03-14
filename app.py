import config.settings

from flask import Flask
from flask_caching import Cache

from flask_admin import Admin, BaseView, expose, AdminIndexView
from flask_admin.contrib.sqla import ModelView

import logging
import logging.config

from apps.book.models import db
from apps.book.models import Book
from apps.book.views.book import book as ebook

app = Flask(__name__)


class MyAdminIndexView(AdminIndexView):
    @expose('/')
    def default(self):
        return self.render('admin_home.html')

admin = Admin(app=app, name=u'后台管理系统', index_view=MyAdminIndexView(u'管理主页'))


class BookList(ModelView):

    can_create = False

    column_list = ('id', 'name','author')
    def __init__(self, session, **kwargs):
        super(BookList, self).__init__(Book, session, **kwargs)

admin.add_view(BookList(db.session, name = u'图书列表'))




logging.config.fileConfig('logging.conf')

redisConfig = {
    'CACHE_TYPE': 'RedisCache',       #使用redis作为缓存
    'CACHE_REDIS_HOST': '127.0.0.1',     #redis地址
    'CACHE_REDIS_PORT': 6379,     #redis端口号
    'CACHE_REDIS_DB': '1'
}
cache = Cache()
#cache.init_app(app=app, config=redisConfig)

def create_app():

    logging.info("[App is starting...]")

    # 装载配置
    app.debug = config.settings.DEBUG
    app.config.update(config.settings.settings)
    # 数据库
    db.app = app
    db.init_app(app)

    #cache.set("test", "test")

    #db.drop_all()
    # 打开之后可以重新建表
    #db.create_all()

    app.register_blueprint(ebook, url_prefix='/ebook')

    return app



if __name__ == '__main__':
    create_app().run()

