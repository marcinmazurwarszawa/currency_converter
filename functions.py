from decimal import *

import requests

from exceptions import CustomException
from settings import NBP_BASE_CURRENCY_URL
from repositories import find_actual_exchange_rate_in_db, save_actual_exchange_rate


def download_exchange_rate(curr_code: str) -> Decimal:
    url = f'{NBP_BASE_CURRENCY_URL}{curr_code}?format=json'
    try:
        resp = requests.get(url)
        if resp.status_code == 404:
            raise CustomException("Wrong currency code")
        rate = resp.json()['rates'][0]['mid']
    except KeyError:
        raise CustomException("Problem with external service", 503)
    return Decimal(str(rate))


def get_exchange_rate(curr: str) -> Decimal:
    curr = curr.upper()
    if curr == 'PLN':
        return Decimal(1)
    rate = find_actual_exchange_rate_in_db(curr=curr)
    if rate is None:
        rate = download_exchange_rate(curr_code=curr)
        save_actual_exchange_rate(curr=curr, rate=rate)
    return rate


def convert_to_another_currency(amount: str, curr_1: str, curr_2: str) -> Decimal:
    try:
        amount = Decimal(amount)
    except TypeError:
        raise CustomException('Wrong amount to convert')
    curr_1_to_pln = get_exchange_rate(curr=curr_1)
    pln_to_curr_2 = get_exchange_rate(curr=curr_2)
    return amount * curr_1_to_pln * pln_to_curr_2
