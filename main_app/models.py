from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    bodystyle = models.CharField(max_length=100)

def __str__(self):
    return self.name
