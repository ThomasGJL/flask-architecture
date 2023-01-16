import os

DEBUG = True

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

settings = {
    'SQLALCHEMY_DATABASE_URI': '',
    'SQLALCHEMY_TRACK_MODIFICATIONS': True,
}
