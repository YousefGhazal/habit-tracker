from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    check_password = models.CharField(max_length=200)

class Habit(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Done(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    done = models.BooleanField()