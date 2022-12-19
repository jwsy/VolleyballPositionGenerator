from django.db import models
from django.urls import reverse

# Create your models here.


class Position(models.Model):
    # POSITION = (
    #     ('Libero', 'Libero'),
    #     ('Hitter', 'Hitter'),
    #     ('Setter', 'Setter'),
    # )
    # name = models.CharField(choices=POSITION, max_length=20)
    name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)


class Player(models.Model):
    name = models.CharField(max_length=100,
                            unique=True,
                            help_text='Player name')
    position = models.ManyToManyField(Position, null=True)
    favorite_ice_cream = models.CharField(max_length=50, blank=True)

    def get_positions(self):
        return ",".join([str(p) for p in self.position.all()])