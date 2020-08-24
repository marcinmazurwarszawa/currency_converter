from flask import request, jsonify

from exceptions import CustomException
from settings import app
from services import CurrencyConverterService


@app.route('/convert', methods=['GET'])
def convert():
    curr_1 = request.args.get('currency1')
    curr_2 = request.args.get('currency2')
    amount = request.args.get('amount')
    if curr_1 is None or curr_2 is None:
        raise CustomException('Both currency1 and currency2 are needed')
    converter = CurrencyConverterService()
    converted = converter.convert(amount=amount, curr_1=curr_1, curr_2=curr_2)
    payload = {
        'currency1': curr_1,
        'currency2': curr_2,
        'amount': amount,
        'converted': converted,
    }
    return jsonify(payload)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
