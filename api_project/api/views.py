from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

# ✅ List-only view (read-only)
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# ✅ Full CRUD viewset
class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides create, retrieve, update, and delete operations on Book model.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
