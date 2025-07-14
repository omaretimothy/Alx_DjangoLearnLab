# Create

>>> from bookshelf.models import Book
>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
>>> book
# <Book: 1984>

# Retrieve

>>> from bookshelf.models import Book
>>> book = Book.objects.get(title="1984")
>>> book.title, book.author, book.publication_year
# ('1984', 'George Orwell', 1949)

# Update

>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> book.title
# 'Nineteen Eighty-Four'

# Delete

>>> book.delete()
>>> Book.objects.all()
# <QuerySet []>
