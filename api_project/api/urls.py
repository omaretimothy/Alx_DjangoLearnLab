from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import BookList, BookViewSet

# Create and configure router
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # List view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),

    # Token auth endpoint (POST username & password → receive token)
    path('auth/token/', obtain_auth_token, name='api_token_auth'),

    # Include router-generated CRUD routes
    path('', include(router.urls)),
]
