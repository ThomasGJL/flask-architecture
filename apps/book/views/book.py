from flask import Blueprint
from flask import redirect
from flask import render_template
from flask import request

from apps.book.models import Book, Booktag, db

book = Blueprint('ebook', __name__)

@book.route('/show_entries')
def show_entries():
    books = Book.query.order_by(Book.id.desc()).all()
    return render_template('show_entries.html', entries=books)

@book.route('/show_books')
def show_books():
    books = Book.query.join(Booktag, Book.tid == Booktag.id).add_columns(Book.id, Book.name, Book.author, Booktag.tag_name).all()
    return render_template('show_books.html', entries=books)

@book.route('/delete', methods=['GET'])
def delete():
    entry = Book.query.get(request.args.get("id"))
    db.session.delete(entry)
    db.session.commit()

    return redirect('/ebook/show_entries')
