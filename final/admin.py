from django.contrib import admin
from .models import Book, Journal


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'num_pages')


@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type')

