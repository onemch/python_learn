from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.secret_key = '123456'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/flask_books'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)


class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)

    books = db.relationship('Book', backref='author')

    def __repr__(self):
        return f'Author: {self.name}'


class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))

    def __repr__(self):
        return f'Book: {self.name}  {self.author_id} '

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'author': self.author.name
        }


@app.route('/getbook', methods=['GET', 'POST'])
def getBook():

    books = Book.query.join(Author)
    for key, value in request.args.items():
        if key == 'author':
            books = books.filter(
                Author.__getattribute__(Author, 'name').like(
                    f'%{value}%' if value else '%%'))
        else:
            books = books.filter(
                Book.__getattribute__(Book, key).like(
                    f'%{value}%' if value else '%%'))

    books = books.all()

    ret = {'books': []}
    for book in books:
        ret['books'].append(book.to_json())
    print(ret)
    return ret


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        authorArg = request.form.get('author')
        bookArg = request.form.get('book')
        findAuthorByName = Author.query.filter_by(name=authorArg).first()
        if findAuthorByName:
            book = Book.query.filter_by(name=bookArg).first()
            if book:
                flash('已存在同名书籍')
            else:
                try:
                    new_book = Book(
                        name=bookArg, author_id=findAuthorByName.id)
                    db.session.add(new_book)
                    db.session.commit()
                except Exception as e:
                    print(e)
                    flash('添加书籍失败')
                    db.session.rollback()

        else:
            try:
                new_author = Author(name=authorArg)
                db.session.add(new_author)
                db.session.commit()
                new_book = Book(name=bookArg, author_id=new_author.id)
                db.session.add(new_book)
                db.session.commit()

            except Exception as e:
                print(e)
                flash('添加书籍或作者失败')
                db.session.rollback()

    authors = Author.query.all()

    return render_template('books.html', authors=authors)


@app.route('/delete_book/<id>')
def delete_book(id):
    book = Book.query.get(id)

    if book:
        try:
            db.session.delete(book)
            db.session.commit()
        except Exception as e:
            print(e)
            flash('删除书籍错误')
            db.session.rollback()
    else:
        flash('找不到书籍')

    return redirect(url_for('index'))


@app.route('/delete_author/<id>')
def delete_author(id):
    author = Author.query.get(id)

    if author:
        try:
            Book.query.filter_by(author_id=id).delete()
            db.session.delete(author)
            db.session.commit()
        except Exception as e:
            print(e)
            flash('删除作者错误')
            db.session.rollback()
    else:
        flash('找不到作者')

    return redirect(url_for('index'))


if __name__ == "__main__":

    db.drop_all()
    db.create_all()

    au1 = Author(name='123')
    au2 = Author(name='456')
    au3 = Author(name='789')
    au4 = Author(name='2333')
    au5 = Author(name='2www')
    au6 = Author(name='3rrrr')
    db.session.add_all([au1, au2, au3, au4, au5, au6])
    db.session.commit()

    bk1 = Book(name='qwe', author_id=au1.id)
    bk2 = Book(name='asd', author_id=au2.id)
    bk3 = Book(name='zxc', author_id=au3.id)
    bk4 = Book(name='rty', author_id=au4.id)
    bk5 = Book(name='fgh', author_id=au5.id)
    bk6 = Book(name='qddd', author_id=au6.id)
    bk7 = Book(name='qsss', author_id=au1.id)
    db.session.add_all([bk1, bk2, bk3, bk4, bk5, bk6, bk7])
    db.session.commit()

    app.run(debug=True)
