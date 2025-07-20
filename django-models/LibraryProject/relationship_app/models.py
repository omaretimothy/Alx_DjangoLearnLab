from django.db import models

# Author can write many books
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Each Book is written by ONE author (ForeignKey)
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# A Library can have MANY books (ManyToMany)
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

# Each Library has exactly ONE Librarian (OneToOne)
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
from django.db import models

# Create your models here.
