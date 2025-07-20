from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Book
from .models import Library

# ✅ Function-based view to list all books (protected)
@login_required
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# ✅ Class-based view to display library details (protected)
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# ✅ Register view
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto-login after registration
            return redirect('list_books')  # redirect after success
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# ✅ Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list_books')  # redirect after login
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

# ✅ Logout view
def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')
