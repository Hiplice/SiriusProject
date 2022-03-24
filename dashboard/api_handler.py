import json
import requests


def get_access_token(client_id):
    url = "https://sb0.test.openbankingrussia.ru/sandbox0/as/aft/connect/token"

    payload = f'client_id={client_id}&grant_type=client_credentials&scope=accounts&state=e0d8e246-a46f-4352-b581-4f1d0d0df6c4'
    headers = {
        'Authorization': 'Basic MDU2OWZlMWU2NWM2NDA1ZjhhZWJhNWQ3M2JjMzg3ZTI6WWhZUUVrRTJReXlpaEoyekpSSXNJRDlFUDE5WjlJWnU=',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    return json.loads(requests.request("POST", url, headers=headers, data=payload, verify=False).text)


def create_consent(access_token):
    url = "https://sb0.test.openbankingrussia.ru/sandbox0/open-banking/v1.2/aisp/account-consents"

    payload = json.dumps({
        "Data": {
            "permissions": [
                "ReadAccountsBasic",
                "ReadBalances",
                "ReadTransactionsCredits",
                "ReadTransactionsDebits",
                "ReadTransactionsDetail",
                "ReadTransactionsBasic"
            ],
            "expirationDateTime": "2024-10-03T00:00:00+00:00",
            "transactionFromDateTime": "2019-01-01T00:00:00+00:00",
            "transactionToDateTime": "2024-12-31T00:00:00+00:00"
        },
        "Risk": {}
    })
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    return json.loads(response.text)


def get_accounts(auth):
    url = "https://sb0.test.openbankingrussia.ru/sandbox0/open-banking/v1.2/aisp/accounts"
    payload={}
    headers = {
        'Authorization': auth
        }
    response = requests.request("GET", url, headers=headers, data=payload, verify=False)
    return json.dumps(response.text)


def get_transactions(auth):
    url = "https://sb0.test.openbankingrussia.ru/sandbox0/open-banking/v1.2/aisp/transactions"
    payload={}
    headers = {
        'Authorization': auth
        }
    response = requests.request("GET", url, headers=headers, data=payload, verify=False)
    return json.dumps(response.text)


def get_balances(auth):
    url = "https://sb0.test.openbankingrussia.ru/sandbox0/open-banking/v1.2/aisp/balances"
    payload={}
    headers = {
        'Authorization': auth
        }
    response = requests.request("GET", url, headers=headers, data=payload, verify=False)
    return json.dumps(response.text)