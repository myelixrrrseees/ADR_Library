from app import db
from models import Book
import json

with open("books.json") as f:
    books = json.load(f)
    for book in books:
        book = Book(title='title', author='author', language='language', year='year', pages='pages')

        db.session.add(book)
        db.session.commit()