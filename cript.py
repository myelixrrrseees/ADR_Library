from app import Book
from app import db
import json
books_json = json.load(open('books.json'))
for book in books_json:
    book = Book(title=book['title'], author=book['author'], language=book['language'], year=book['year'],
                pages=book['pages'])
    db.session.add(book)
db.session.commit()
