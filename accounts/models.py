from django.db import models
from django.contrib.auth import models as auth_models


class User(auth_models.User):
    banks = models.ForeignKey('dashboard.BankUser', on_delete=models.CASCADE)