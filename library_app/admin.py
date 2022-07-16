from django.contrib import admin
from .models import Book
# Register your models here.
from django.contrib.auth.models import User

class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Book, BookAdmin)

