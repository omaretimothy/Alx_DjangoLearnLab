from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, CustomUser, UserProfile

# Custom admin for Book
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('publication_year',)
    search_fields = ('title', 'author')

# Custom admin for CustomUser
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'date_of_birth', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {'fields': ('date_of_birth', 'profile_photo')}),
    )

# Custom admin for UserProfile
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    list_filter = ('role',)
    search_fields = ('user__username', 'role')

# Registering the models
admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
