import unittest
import json
from pyfinance_server import app


class TestEndpointsResponseCodes(unittest.TestCase):
    def test_info(self):
        response = app.test_client().get('/tickers/msft/info')
        info = json.loads(response.data)
        self.assertEqual(response.status, '200 OK')
        self.assertIsNotNone(info)
        self.assertIsNotNone(info['trailingPE'])

    def test_institutional_holders(self):
        response = app.test_client().get('/tickers/msft/institutional-holders')
        json.loads(response.data)
        self.assertEqual(response.status, '200 OK')

    def test_actions(self):
        response = app.test_client().get('/tickers/msft/actions')
        json.loads(response.data)
        self.assertEqual(response.status, '200 OK')

    def test_dividends(self):
        response = app.test_client().get('/tickers/msft/dividends')
        json.loads(response.data)
        self.assertEqual(response.status, '200 OK')

    def test_splits(self):
        response = app.test_client().get('/tickers/msft/splits')
        json.loads(response.data)
        self.assertEqual(response.status, '200 OK')

    def test_major_holders(self):
        response = app.test_client().get('/tickers/msft/major-holders')
        json.loads(response.data)
        self.assertEqual(response.status, '200 OK')

    def test_cashflow(self):
        response = app.test_client().get('/tickers/msft/cashflow')
        json.loads(response.data)
        self.assertEqual(response.status, '200 OK')

    def test_quarterly_cashflow(self):
        response = app.test_client().get('/tickers/msft/quarterly-cashflow')
        json.loads(response.data)
        self.assertEqual(response.status, '200 OK')

    def test_earnings(self):
        response = app.test_client().get('/tickers/msft/earnings')
        json.loads(response.data)
        self.assertEqual(response.status, '200 OK')

    def test_quarterly_earnings(self):
        response = app.test_client().get('/tickers/msft/quarterly-earnings')
        json.loads(response.data)
        self.assertEqual(response.status, '200 OK')

    def test_sustainability(self):
        response = app.test_client().get('/tickers/msft/sustainability')
        json.loads(response.data)
        self.assertEqual(response.status, '200 OK')

    def test_recommendations(self):
        response = app.test_client().get('/tickers/msft/recommendations')
        json.loads(response.data)
        self.assertEqual(response.status, '200 OK')

    def test_calendar(self):
        response = app.test_client().get('/tickers/msft/calendar')
        json.loads(response.data)
        self.assertEqual(response.status, '200 OK')

    def test_isin(self):
        response = app.test_client().get('/tickers/msft/isin')
        json.loads(response.data)
        self.assertEqual(response.status, '200 OK')

    def test_options(self):
        response = app.test_client().get('/tickers/msft/options')
        json.loads(response.data)
        self.assertEqual(response.status, '200 OK')

    def test_nonexistent_endpoint(self):
        response = app.test_client().get('/tickers/msft/does-not-exist')
        self.assertEqual(response.status, '404 NOT FOUND')

    def test_all(self):
        response = app.test_client().get('/tickers/')
        stocks_dict = json.loads(response.data)
        self.assertEqual(response.status, '200 OK')
        self.assertIsNotNone(stocks_dict['stocks'])
        self.assertIsNotNone(stocks_dict['stocks']['AAL'])
        self.assertIsNotNone(stocks_dict['stocks']['AAL']['info'])
        self.assertIsNotNone(stocks_dict['stocks']['AAL']['info']['trailingPE'])

    def test_trailing_pe(self):
        response = app.test_client().get('/tickers/sort?sort-by=forwardPE')
        json.loads(response.data)
        self.assertEqual(response.status, '200 OK')


if __name__ == '__main__':
    unittest.main()
