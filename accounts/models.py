from django.db import models
from django.contrib.auth import models as auth_models


class User(auth_models.AbstractUser):
    banks = models.ManyToManyField(to='dashboard.BankUser')
    client_id = models.CharField(max_length=128)
    client_secret = models.CharField(max_length=128)
    consent_uri = models.CharField(max_length=1024, null=True, blank=True)
