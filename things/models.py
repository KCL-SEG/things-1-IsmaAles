from django.db import models
from django.db.models import Model

class Thing(Model):
    name = models.CharField(
        max_length = 15,
    )
    description = models.CharField(
        max_length = 30,
    )
    quantity = models.IntegerField()