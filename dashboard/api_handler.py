import json
import requests
import urllib3
import sqlite3


def connect_db():
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("База данных создана и успешно подключена к SQLite")

        sqlite_select_query = "select sqlite_version();"
        cursor.execute(sqlite_select_query)
        record = cursor.fetchall()
        print("Версия базы данных SQLite: ", record)
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
    urllib3.disable_warnings()


def getAccounts(auth):
    url = "https://sb0.test.openbankingrussia.ru/sandbox0/open-banking/v1.2/aisp/accounts"
    payload={}
    headers = {
        'Authorization': auth
        }
    response = requests.request("GET", url, headers=headers, data=payload, verify=False)
    return json.dumps(response.text)


def getTransactions(auth):
    url = "https://sb0.test.openbankingrussia.ru/sandbox0/open-banking/v1.2/aisp/transactions"
    payload={}
    headers = {
        'Authorization': auth
        }
    response = requests.request("GET", url, headers=headers, data=payload, verify=False)
    return json.dumps(response.text)


def getBalances(auth):
    url = "https://sb0.test.openbankingrussia.ru/sandbox0/open-banking/v1.2/aisp/balances"
    payload={}
    headers = {
        'Authorization': auth
        }
    response = requests.request("GET", url, headers=headers, data=payload, verify=False)
    return json.dumps(response.text)