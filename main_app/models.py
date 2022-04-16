from django.db import models
from django.urls import reverse

CLEANING = (
    ('M', 'Morning'), 
    ('MD', "Mid-Day"), 
    ('N', 'Night')
)

class Car(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    bodystyle = models.CharField(max_length=100)

def __str__(self):
    return self.name

def get_absolute_url(self):
    return reverse('detail', kwargs={'car_id': self.id})

class Cleaning(models.Model):
    date = models.DateField()
    cleantime = models.CharField(max_length=100, choices=CLEANING, default=None)

cat = models.ForeignKey(
    Car,
    on_delete=models.CASCADE
)

def __str__(self):
    return f"{self.get_cleantime_display()} on {self.date}"

class Meta:
    ordering = ['-date']