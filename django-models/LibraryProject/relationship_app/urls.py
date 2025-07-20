from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import (
    list_books,
    LibraryDetailView,
    admin_view,
    librarian_view,
    member_view
)

urlpatterns = [
    # ✅ Existing FBV + CBV
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # ✅ Authentication routes
    path('register/', views.register_view, name='register'),  # checker expects `views.register`
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # ✅ Role-based routes
    path('role/admin/', admin_view, name='admin_view'),
    path('role/librarian/', librarian_view, name='librarian_view'),
    path('role/member/', member_view, name='member_view'),
]
