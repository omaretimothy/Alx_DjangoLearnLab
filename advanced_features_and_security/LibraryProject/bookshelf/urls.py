from django.urls import path
from .views import book_list

urlpatterns = [
    path('bookshelf/books/', book_list, name='bookshelf_book_list'),
]
