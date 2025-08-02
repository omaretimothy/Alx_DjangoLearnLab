from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Create and configure router
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # List view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),

    # Include router-generated CRUD routes
    path('', include(router.urls)),
]
