from sqlalchemy import Column, String, Date, DECIMAL

from settings import db


class ExchangeRate(db.Model):
    __tablename__ = 'exchange_rate'

    currency = Column(String(3), nullable=False, primary_key=True)
    day = Column(Date, nullable=False, primary_key=True)
    rate = Column(DECIMAL, nullable=False)
