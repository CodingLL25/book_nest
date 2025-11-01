from django.contrib import admin
from .models import Collection, Book, Tag

# Register your models here.
admin.site.register(Collection)
admin.site.register(Book)
admin.site.register(Tag)
