import os

DEBUG = True

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

settings = {
    'SQLALCHEMY_DATABASE_URI': 'mysql+pymysql://root:123456@localhost:3306/flask_demo',
    'SQLALCHEMY_TRACK_MODIFICATIONS': True,
}