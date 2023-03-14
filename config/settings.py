import os

DEBUG = True

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

settings = {
    #'SQLALCHEMY_DATABASE_URI': 'mysql+pymysql://root:123456@localhost:3306/flask_demo',
    'SQLALCHEMY_DATABASE_URI': 'postgresql://postgres:admin@localhost:5432/database',
    'SQLALCHEMY_TRACK_MODIFICATIONS': True,
}
