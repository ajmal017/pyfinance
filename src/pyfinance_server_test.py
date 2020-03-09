import unittest
from pyfinance_server import app


class TestEndpointsResponseCodes(unittest.TestCase):
    def test_info(self):
        response = app.test_client().get('/tickers/msft/info')
        self.assertEqual(response.status, '200 OK')

    def test_institutional_holders(self):
        response = app.test_client().get('/tickers/msft/institutional-holders')
        self.assertEqual(response.status, '200 OK')

    def test_actions(self):
        response = app.test_client().get('/tickers/msft/actions')
        self.assertEqual(response.status, '200 OK')

    def test_dividends(self):
        response = app.test_client().get('/tickers/msft/dividends')
        self.assertEqual(response.status, '200 OK')

    def test_splits(self):
        response = app.test_client().get('/tickers/msft/splits')
        self.assertEqual(response.status, '200 OK')

    def test_major_holders(self):
        response = app.test_client().get('/tickers/msft/major-holders')
        self.assertEqual(response.status, '200 OK')

    def test_cashflow(self):
        response = app.test_client().get('/tickers/msft/cashflow')
        self.assertEqual(response.status, '200 OK')

    def test_quarterly_cashflow(self):
        response = app.test_client().get('/tickers/msft/quarterly-cashflow')
        self.assertEqual(response.status, '200 OK')

    def test_earnings(self):
        response = app.test_client().get('/tickers/msft/earnings')
        self.assertEqual(response.status, '200 OK')

    def test_quarterly_earnings(self):
        response = app.test_client().get('/tickers/msft/quarterly-earnings')
        self.assertEqual(response.status, '200 OK')

    def test_sustainability(self):
        response = app.test_client().get('/tickers/msft/sustainability')
        self.assertEqual(response.status, '200 OK')

    def test_recommendations(self):
        response = app.test_client().get('/tickers/msft/recommendations')
        self.assertEqual(response.status, '200 OK')

    def test_calendar(self):
        response = app.test_client().get('/tickers/msft/calendar')
        self.assertEqual(response.status, '200 OK')

    def test_isin(self):
        response = app.test_client().get('/tickers/msft/isin')
        self.assertEqual(response.status, '200 OK')

    def test_options(self):
        response = app.test_client().get('/tickers/msft/options')
        self.assertEqual(response.status, '200 OK')

    def test_nonexistent_endpoint(self):
        response = app.test_client().get('/tickers/msft/does-not-exist')
        self.assertEqual(response.status, '404 NOT FOUND')


if __name__ == '__main__':
    unittest.main()
