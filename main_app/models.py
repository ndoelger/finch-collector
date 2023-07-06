from django.db import models

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    alive = models.BooleanField()

    def __str__(self):
        return f'{self.name} ({self.id})'