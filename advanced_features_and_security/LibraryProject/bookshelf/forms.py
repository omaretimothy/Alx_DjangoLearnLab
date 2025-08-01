from django import forms
from .models import Book

# A basic form for testing or demonstration purposes
class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name")
    message = forms.CharField(widget=forms.Textarea, label="Message")

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
