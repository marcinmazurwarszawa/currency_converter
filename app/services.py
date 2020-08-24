from decimal import Decimal, DecimalException

import requests

from exceptions import CustomException
from settings import NBP_BASE_CURRENCY_URL, RETURN_PRECISION
from repositories import find_actual_exchange_rate_in_db, save_actual_exchange_rate


class ExchangeRateService:
    CURRENCY_PLN = 'PLN'

    def __init__(self, curr: str):
        self.curr = curr.upper()

    def get_exchange_rate(self) -> Decimal:
        if self.curr == self.CURRENCY_PLN:
            return Decimal(1)
        rate = find_actual_exchange_rate_in_db(curr=self.curr)
        if rate is None:
            rate = self.__download_exchange_rate()
            save_actual_exchange_rate(curr=self.curr, rate=rate)
        return rate

    def __download_exchange_rate(self) -> Decimal:
        url = f'{NBP_BASE_CURRENCY_URL}{self.curr}?format=json'
        try:
            resp = requests.get(url)
            if resp.status_code == 404:
                raise CustomException("Wrong currency code")
            rate = resp.json()['rates'][0]['mid']
        except KeyError:
            raise CustomException("Problem with external service", 503)
        return Decimal(str(rate))


class CurrencyConverterService:

    def convert(self, amount: str, curr_1: str, curr_2: str) -> float:
        try:
            amount = Decimal(amount)
        except (TypeError, DecimalException):
            raise CustomException('Wrong amount to convert')
        exchange_service_curr_1 = ExchangeRateService(curr=curr_1)
        curr_1_to_pln = exchange_service_curr_1.get_exchange_rate()
        exchange_service_curr_2 = ExchangeRateService(curr=curr_2)
        pln_to_curr_2 = exchange_service_curr_2.get_exchange_rate()
        converted = amount * curr_1_to_pln / pln_to_curr_2
        return round(float(converted), RETURN_PRECISION)
