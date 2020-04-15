from django.contrib import admin
from .models import Book
from .models import Author
from .models import Tag

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Tag)
