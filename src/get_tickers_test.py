import unittest
from . helpers import get_tickers


class TestEndpointsResponseCodes(unittest.TestCase):
    def test_info(self):
        tickers = get_tickers()
        self.assertEqual(len(tickers), 270)


if __name__ == '__main__':
    unittest.main()
