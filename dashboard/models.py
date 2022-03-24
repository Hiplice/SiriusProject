from django.db import models


class Transaction(models.Model):
    sum = models.SmallIntegerField()
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)


class BankAccount(models.Model):
    account_name = models.CharField(max_length=20)
    sum = models.SmallIntegerField()
    transactions = models.ForeignKey('Transaction', on_delete=models.CASCADE)


class BankUser(models.Model):
    accounts = models.ForeignKey('BankAccount', on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=20)
