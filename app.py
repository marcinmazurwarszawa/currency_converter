from flask import request, jsonify

from settings import app, RETURN_PRECISION
from functions import convert_to_another_currency


@app.route('/convert', methods=['GET'])
def convert():
    curr_1 = request.args.get('currency1')
    curr_2 = request.args.get('currency2')
    amount = request.args.get('amount')
    converted = convert_to_another_currency(amount=amount, curr_1=curr_1, curr_2=curr_2)
    converted = round(float(converted), RETURN_PRECISION)
    payload = {
        'currency1': curr_1,
        'currency2': curr_2,
        'amount': amount,
        'value2': converted,
    }
    return jsonify(payload)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
