from django.db import models


# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    organizer_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
