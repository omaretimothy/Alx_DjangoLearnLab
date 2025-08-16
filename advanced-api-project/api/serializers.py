from rest_framework import serializers
from .models import Author, Book
from datetime import datetime


class BookSerializer(serializers.ModelSerializer):
    """
    Serializes the Book model, ensuring the publication year is not in the future.
    """
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        if value > datetime.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes the Author model, including all related books using nested BookSerializer.
    """
    books = BookSerializer(many=True, read_only=True)  # Related name from the model

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
