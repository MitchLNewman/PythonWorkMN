from application import app2
from flask import request
from flask import render_template
from random import choice
from book import Book


@app2.route('/')
def index():
    return "Library System"


'''
@app.route('/generate/<int:num>')
def generate(num: int):
    return [{"firstname":choice(first_names), "lastname":choice(last_names)} for i in range(num)]
'''


@app2.route('/add')
def generate():
    title = request.args.get("title")
    pages = int(request.args.get("pages"))
    isbn = request.args.get("isbn")
    genre = request.args.get("genre")
    author = request.args.get("author")

    new_book = Book(title, pages, isbn, genre, author)

    return "New book added!"


@app2.route('/view')
def get_books():
    books = Book.get_books()

    for book in books:
        print(book)

    return "Books printed in the console."

@app2.route("/search")
def search_books():
    author=request.args.get("author")

    books = Book.search(author)
    string = ''
    if len(books) == 0:
        return "No books by this author!"
    elif len(books) > 0:
        for book in books:
            string += (book.title + "\n")
        return string
    
@app2.route("/update")
def update_books():
    pass