from django.shortcuts import HttpResponse, render, redirect
from django.contrib.auth.decorators import login_required
from .api_handler import *
from .models import *


@login_required(login_url='login/')
def load_dashboard(request):
    transactions = Transaction.objects.all()
    bank_accounts = BankAccount.objects.all()
    return render(request, 'dashboard/dashboard.htm',
                  context={'acc_amount': range(1, len(bank_accounts) + 1),
                           'transactions': transactions})


@login_required(login_url='login/')
def get_consent(request):
    if not request.POST:
        return render(request, 'dashboard/redirect.html')
    else:
        if request.POST['error'] == 'undefined':
            data = get_hybrid_token(request.user.client_id, request.user.client_secret, request.POST['code'])

            # Creating bank id
            new_bank = BankUser(bank_name='Банк', token=data['access_token'])
            new_bank.save()

            request.user.banks.add(new_bank)
            request.user.save()

            return redirect('/getdata/')
        else:
            return HttpResponse(f'взлом жопы {request.POST["error"]}')


@login_required(login_url='login/')
def get_data(request):
    # Getting banks
    banks = BankUser.objects.all()

    for bank in banks:
        hybrid_token = bank.token
        accounts = get_accounts(hybrid_token)['Data']['Account']
        balances = get_balances(hybrid_token)['Data']['Balance']

        for a_index in range(len(accounts)):
            account = accounts[a_index]
            balance = balances[a_index]

            db_account = BankAccount(account_id=account['accountId'], currency=account['currency'],
                                     amount=float(balance['Amount']['amount']))
            db_account.save()

            # Getting transactions
            transactions = get_transactions(hybrid_token, account['accountId'])['Data']['Transaction']

            for transaction in transactions:
                if not transaction.get('MerchantDetails'):
                    transaction['MerchantDetails'] = {'merchantName': 'Перевод средств'}

                db_transaction = Transaction(description=transaction['transactionInformation'],
                                             name=transaction['MerchantDetails']['merchantName'],
                                             amount=transaction['Amount']['amount'])
                db_transaction.save()

                db_account.transactions.add(db_transaction)
            db_account.save()

            bank.accounts.add(db_account)

        bank.save()

    return redirect('/')
