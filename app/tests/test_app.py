from unittest import TestCase

from app import app


class AppTest(TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_convert_success_content(self):
        params = {'currency1': 'PLN', 'currency2': 'EUR', 'amount': '20'}
        response = self.app.get('/convert', query_string=params)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')

    def test_convert_success_data(self):
        params = {'currency1': 'PLN', 'currency2': 'EUR', 'amount': '20'}
        response = self.app.get('/convert', query_string=params)
        json_data = response.get_json()
        self.assertEqual(len(json_data), 4)
        self.assertEqual(type(json_data), dict)
        self.assertEqual(type(json_data['currency1']), str)
        self.assertEqual(type(json_data['currency2']), str)
        self.assertEqual(type(json_data['amount']), str)
        self.assertEqual(type(json_data['value2']), float)

    def test_convert_no_parameters(self):
        response = self.app.get('/convert')
        self.assertEqual(response.status_code, 400)

    def test_convert_wrong_amount(self):
        params = {'currency1': 'PLN', 'currency2': 'EUR', 'amount': 'aaa'}
        response = self.app.get('/convert', query_string=params)
        self.assertEqual(response.status_code, 400)

    def test_convert_wrong_currency1(self):
        params = {'currency1': 'bbb', 'currency2': 'EUR', 'amount': '30'}
        response = self.app.get('/convert', query_string=params)
        self.assertEqual(response.status_code, 400)

    def test_convert_wrong_currency2(self):
        params = {'currency1': 'PLN', 'currency2': '77', 'amount': '30'}
        response = self.app.get('/convert', query_string=params)
        self.assertEqual(response.status_code, 400)
