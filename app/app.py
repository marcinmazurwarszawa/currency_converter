from flask import request

from exceptions import *
from settings import app, db
from functions import convert_to_another_currency


@app.route('/convert', methods=['GET'])
def convert():
    curr_1 = request.args.get('currency1')
    curr_2 = request.args.get('currency2')
    amount = request.args.get('amount')
    converted = convert_to_another_currency(amount=amount, curr_1=curr_1, curr_2=curr_2)
    payload = {
        'currency1': curr_1,
        'currency2': curr_2,
        'amount': amount,
        'value2': converted,
    }
    return jsonify(payload)


if __name__ == '__main__':
    db.create_all()
    app.run(host="0.0.0.0")