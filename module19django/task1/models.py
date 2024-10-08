from django.db import models


# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=50)
    balance = models.DecimalField()
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField()
    size = models.DecimalField()
    description = models.TextField()
    age_limited = models.BooleanField(1)
    buyer = models.ManyToManyField(Buyer, related_name='game')

    def __str__(self):
        return self.title
