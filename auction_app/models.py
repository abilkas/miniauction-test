from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.db import models

class User(AbstractUser):
    cash_balance = models.PositiveIntegerField(default=0)

class Animal(models.Model):
    ANIMAL_LIST = (
        ('Котик', 'Котик'),
        ('Ежик', 'Ежик'),
    )
    animal = models.CharField('Котик или Ежик', max_length=10, choices=ANIMAL_LIST)
    species = models.CharField('Порода', max_length=50)
    name = models.CharField('Кличка', max_length=50)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Lot(models.Model):
    animals = models.ForeignKey(Animal, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.animals)

    @classmethod
    def create_lot(cls, animals, price, owner):
        return Lot.objects.create(animals=animals, price=price, owner=owner)

class Bet(models.Model):
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE, related_name='bets')
    price = models.PositiveIntegerField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.lot)

    @classmethod
    def make_bet(cls, lot, price, author):
        if lot.owner == cls.author: # чтобы сам автор лота не мог сделать ставку
            raise ValidationError

        return Bet.objects.create(lot=lot, price=price, author=author)

