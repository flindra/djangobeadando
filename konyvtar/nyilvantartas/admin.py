from django.contrib import admin

# Register your models here.
from .models import Author, Book, User, Lending

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(User)
admin.site.register(Lending)