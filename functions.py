from decimal import *

import requests

from settings import NBP_BASE_CURRENCY_URL


def download_exchange_rate(curr_code: str) -> Decimal:
    url = f'{NBP_BASE_CURRENCY_URL}{curr_code}?format=json'
    try:
        resp = requests.get(url)
        if resp.status_code == 404:
            raise Exception("Wrong currency code")
        rate = resp.json()['rates'][0]['mid']
    except ValueError:
        raise Exception("Problem with external service")
    return Decimal(rate)


def get_exchange_rate(curr: str) -> Decimal:
    if curr.upper() == 'PLN':
        return Decimal(1)
    exchange_rate = download_exchange_rate(curr_code=curr)
    return exchange_rate


def convert_to_another_currency(amount: str, curr_1: str, curr_2: str) -> Decimal:
    try:
        amount = Decimal(amount)
    except TypeError:
        raise Exception('Wrong amount to convert')
    curr_1_to_pln = get_exchange_rate(curr=curr_1)
    pln_to_curr_2 = get_exchange_rate(curr=curr_2)
    return amount * curr_1_to_pln * pln_to_curr_2
