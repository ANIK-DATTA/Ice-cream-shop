from django.db import models

# Create your models here.
class Contact (models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    msg = models.TextField(max_length=500)
    date = models.DateField()

    def __str__(self):
        return self.name
