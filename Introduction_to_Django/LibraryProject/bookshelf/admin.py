from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # show these columns in list view
    list_filter = ('publication_year',)                     # filter sidebar
    search_fields = ('title', 'author')                     # search box

admin.site.register(Book, BookAdmin)
