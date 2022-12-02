from models import db
from models import Book
import json

with open("books.json", encoding="utf8") as f:
    books = json.load(f)
    for book in books:
        book = Book(title=book['title'], author=book['author'], language=book['language'], year=book['year'], pages=book['pages'])

        db.session.add(book)
        db.session.commit()