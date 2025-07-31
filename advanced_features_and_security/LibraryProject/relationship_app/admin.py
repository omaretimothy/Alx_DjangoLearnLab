from django.contrib import admin
from bookshelf.models import CustomUser, UserProfile
from .models import Author, Book, Library, Librarian
from django.contrib.auth.admin import UserAdmin



class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'date_of_birth', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )


# Register other models
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)

