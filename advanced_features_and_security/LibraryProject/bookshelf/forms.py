from django import forms
from .models import Book

class BookSearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        required=False,
        label='Search for books',
        widget=forms.TextInput(attrs={'placeholder': 'Search by title or author'})
    )

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
