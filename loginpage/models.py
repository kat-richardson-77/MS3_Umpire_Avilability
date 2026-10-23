from django.db import models

# Create your models here.
class User(models.Model):
    enid = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    club = models.CharField(max_length=100)
    umpire = models.BooleanField(default=False)
    email = models.EmailField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username