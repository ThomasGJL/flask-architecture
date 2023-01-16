from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Book(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), default="")
    author = db.Column(db.String(20), default="")
    tid = db.Column(db.Integer, db.ForeignKey('booktag.id'), nullable=True)

    __table__name = 'book'


class Booktag(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tag_name = db.Column(db.String(20), default="")
    books = db.relationship('Book')

    __table__name = 'booktag'

