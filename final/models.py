from django.db import models
from django.contrib.auth.models import User


class BookJournalBase(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Book(BookJournalBase):
    num_pages = models.IntegerField()
    genre = models.CharField(max_length=255)


class Journal(BookJournalBase):
    Bullet = 'Bullet'
    Food = 'Food'
    Travel = 'Travel'
    Sport = 'Sport'
    type_choices = [(Bullet, Bullet), (Food, Food), (Travel, Travel), (Sport, Sport)]
    type = models.CharField(max_length=255, choices=type_choices)
    publisher = models.CharField(max_length=255)