from rest_framework import serializers
from django.contrib.auth.models import User

from final.models import Book, Journal


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'price', 'num_pages', 'description', 'genre']


class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ['id', 'name', 'price', 'type', 'publisher', 'description']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'