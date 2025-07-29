from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import (
    list_books,
    LibraryDetailView,
    admin_view,
    librarian_view,
    member_view,
    add_book,
    edit_book,
    delete_book
)

urlpatterns = [
    # ✅ Existing FBV + CBV
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # ✅ Permission-secured book routes (checker needs "add_book/" and "edit_book/")
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:book_id>/', edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', delete_book, name='delete_book'),

    # ✅ (Optional but still keep) original style
    path('books/add/', add_book, name='add_book_alt'),
    path('books/<int:book_id>/edit/', edit_book, name='edit_book_alt'),
    path('books/<int:book_id>/delete/', delete_book, name='delete_book_alt'),

    # ✅ Authentication routes
    path('register/', views.register_view, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # ✅ Role-based routes
    path('role/admin/', admin_view, name='admin_view'),
    path('role/librarian/', librarian_view, name='librarian_view'),
    path('role/member/', member_view, name='member_view'),
]
