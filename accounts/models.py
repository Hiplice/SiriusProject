from django.db import models
from django.contrib.auth import models as auth_models


class User(auth_models.AbstractUser):
    banks = models.ForeignKey('dashboard.BankUser', on_delete=models.CASCADE, null=True, blank=True)
    client_id = models.CharField(max_length=128)
    consent_uri = models.CharField(max_length=1024, null=True, blank=True)
    access_token = models.CharField(max_length=1024, null=True, blank=True)
    hybrid_token = models.CharField(max_length=1024, null=True, blank=True)