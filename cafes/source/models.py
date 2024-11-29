from django.db import models
from django.contrib.auth.models import User

class Cafe(models.Model):
    rating=[
        ('☆','☆'),
       ('☆☆','☆☆'),
        ('☆☆☆','☆☆☆'),
        ('☆☆☆☆','☆☆☆☆'),
       ('☆☆☆☆☆','☆☆☆☆☆'),
    ]

    sockets=[
        (1, 'one'),
        (2, 'tow'),
        (3, 'three'),
        (4, 'four'),
        (5, 'five'),
    ]
    name = models.CharField(max_length=100)
    location = models.TextField(max_length=50)
    open = models.TimeField(null=False)
    close = models.TimeField(null=False)
    coffee = models.CharField(max_length=5, choices=rating, default=0, null=False)
    wifi = models.CharField(max_length=5, choices=rating, default=0, null=False)
    powersockets = models.IntegerField(choices=sockets, default=0, null=False)

    def __str__(self):
        return self.name
