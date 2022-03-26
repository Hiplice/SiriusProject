from django.db import models


class Transaction(models.Model):
    amount = models.FloatField()
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)


class BankAccount(models.Model):
    account_id = models.SmallIntegerField()
    amount = models.FloatField(default=0)
    currency = models.CharField(max_length=10)
    transactions = models.ManyToManyField(to=Transaction)


class BankUser(models.Model):
    accounts = models.ManyToManyField(to=BankAccount)
    bank_name = models.CharField(max_length=50)
    token = models.TextField(null=False)
