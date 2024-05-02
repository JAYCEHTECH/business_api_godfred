from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(unique=True, max_length=250)
    user_id = models.CharField(max_length=250)
    full_name = models.CharField(max_length=250)
    email = models.EmailField()


class MTNTransaction(models.Model):
    user_id = models.CharField(max_length=200, null=False, blank=False)
    amount = models.FloatField(null=False, blank=False, default=0)
    bundle_volume = models.FloatField(null=False, blank=False, default=0)
    status = models.CharField(max_length=200, default="Undelivered")
    batch_id = models.CharField(max_length=200, default="Unknown")
    number = models.CharField(max_length=200, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    firebase_date = models.CharField(max_length=200, null=True, blank=True)


class CashBack(models.Model):
    user_id = models.CharField(max_length=200, null=False, blank=False)
    user_number = models.CharField(max_length=200, null=False, blank=False)
    amount = models.FloatField(null=False, blank=False, default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_id} - {self.amount}"

