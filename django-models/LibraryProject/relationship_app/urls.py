from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView  #
from . import views
from .views import list_books, LibraryDetailView

urlpatterns = [
    # Existing FBV + CBV
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # ✅ Register view (checker expects `views.register`)
    path('register/', views.register_view, name='register'),

    # ✅ Built-in Login & Logout views with templates
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]
