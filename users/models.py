
from django.contrib.auth.models import AbstractUser
from django.db import models

#default balance
default_balance = 1000

class CustomUser(AbstractUser):
    balance = models.BigIntegerField(blank=True, default=default_balance)