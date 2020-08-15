from datetime import date
from decimal import Decimal
from typing import Optional

from models import ExchangeRate
from settings import db


def find_actual_exchange_rate_in_db(curr: str) -> Optional[Decimal]:
    rate = db.session.query(ExchangeRate.rate)\
        .filter(ExchangeRate.currency == curr)\
        .filter(ExchangeRate.day == date.today())\
        .first()
    return rate.rate if rate else None


def save_actual_exchange_rate(curr: str, rate: Decimal) -> None:
    rate = ExchangeRate(currency=curr, day=date.today(), rate=rate)
    db.session.add(rate)
    db.session.commit()
