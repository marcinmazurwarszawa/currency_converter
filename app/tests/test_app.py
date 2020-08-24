import pytest

from app import app


@pytest.mark.parametrize("params, expected_status_code", [
    ({'currency1': 'PLN', 'currency2': 'EUR', 'amount': '20'}, 200),
    ({}, 400),
    ({'currency1': 'PLN', 'currency2': 'EUR', 'amount': 'aaa'}, 400),
    ({'currency1': 'PLN', 'currency2': 'EUR'}, 400),
    ({'currency1': 'bbb', 'currency2': 'EUR', 'amount': '30'}, 400),
    ({'currency2': 'EUR', 'amount': '30'}, 400),
    ({'currency1': 'PLN', 'currency2': '77', 'amount': '30'}, 400),
    ({'currency1': 'PLN', 'amount': '30'}, 400),
])
def test_convert_response_status_code(params, expected_status_code):
    client = app.test_client()
    response = client.get('/convert', query_string=params)
    assert response.status_code == expected_status_code
    assert response.content_type == 'application/json'


def test_convert_success_data():
    client = app.test_client()
    params = {'currency1': 'PLN', 'currency2': 'EUR', 'amount': '20'}
    response = client.get('/convert', query_string=params)
    json_data = response.get_json()
    assert len(json_data) == 4
    assert type(json_data) == dict
    assert type(json_data['currency1']) == str
    assert type(json_data['currency2']) == str
    assert type(json_data['amount']) == str
    assert type(json_data['converted']) == float
