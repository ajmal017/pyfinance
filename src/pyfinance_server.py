from flask import Flask, request
import yfinance as yf
from pandas import Timestamp
import json
from tqdm import tqdm
from urllib.error import HTTPError
import multiprocessing
from joblib import Parallel, delayed
from helpers import get_tickers


app = Flask(__name__)


@app.route("/tickers/<string:ticker>/info")
def info(ticker):
    return yf.Ticker(ticker).info


@app.route("/tickers/<string:ticker>/institutional-holders")
def institutional_holders(ticker):
    return yf.Ticker(ticker).institutional_holders.to_json()


@app.route("/tickers/<string:ticker>/actions")
def actions(ticker):
    return yf.Ticker(ticker).actions.to_json()


@app.route("/tickers/<string:ticker>/dividends")
def dividends(ticker):
    return yf.Ticker(ticker).dividends.to_json()


@app.route("/tickers/<string:ticker>/splits")
def splits(ticker):
    return yf.Ticker(ticker).splits.to_json()


@app.route("/tickers/<string:ticker>/major-holders")
def major_holders(ticker):
    return yf.Ticker(ticker).major_holders.to_json()


@app.route("/tickers/<string:ticker>/cashflow")
def cashflow(ticker):
    return yf.Ticker(ticker).cashflow.to_json()


@app.route("/tickers/<string:ticker>/quarterly-cashflow")
def quarterly_cashflow(ticker):
    return yf.Ticker(ticker).quarterly_cashflow.to_json()


@app.route("/tickers/<string:ticker>/earnings")
def earnings(ticker):
    return yf.Ticker(ticker).earnings.to_json()


@app.route("/tickers/<string:ticker>/quarterly-earnings")
def quarterly_earnings(ticker):
    return yf.Ticker(ticker).quarterly_earnings.to_json()


@app.route("/tickers/<string:ticker>/sustainability")
def sustainability(ticker):
    return yf.Ticker(ticker).sustainability.to_json()


@app.route("/tickers/<string:ticker>/recommendations")
def recommendations(ticker):
    response = yf.Ticker(ticker).recommendations
    response.reset_index(drop=True, inplace=True)
    return response.to_json()


@app.route("/tickers/<string:ticker>/calendar")
def calendar(ticker):
    return yf.Ticker(ticker).calendar.to_json()


@app.route("/tickers/<string:ticker>/isin")
def isin(ticker):
    return json.dumps({"isin": yf.Ticker(ticker).isin})


@app.route("/tickers/<string:ticker>/options")
def options(ticker):
    return json.dumps({"options": list(yf.Ticker(ticker).options)})


@app.route("/tickers/")
def all_tickers():
    def run(t):
        try:
            return yf.Ticker(t).to_dict()
        except HTTPError:
            pass

    num_cores = multiprocessing.cpu_count()
    response = Parallel(n_jobs=num_cores)(delayed(run)(t) for t in tqdm(get_tickers()))
    new_dict = {}
    for item in response:
        key = item['info']['symbol']
        new_dict[key] = item
    return json.dumps({"stocks": new_dict})


@app.route("/tickers/sort")
def trailing_pe_sorted():
    sort_by = request.args.get('sort-by')

    def the_key(x):
        try:
            value = stocks[x]['info'][sort_by]
            return float(value) if value is not None else 9999
        except KeyError:
            return 99999

    stocks = json.loads(all_tickers())['stocks']
    sorted_stocks = {}
    for ticker in sorted(stocks.keys(), key=the_key):
        try:
            info = stocks[ticker]['info']
            sorted_stocks[ticker] = {
                'short_name': info['shortName'],
                'trailing_pe': info['trailingPE'],
                'forward_pe': info['forwardPE'],
                'regular_market_price': info['regularMarketPrice'],
                'two_hundred_day_average': info['twoHundredDayAverage'],
                'fifty_two_week_low': info['fiftyTwoWeekLow'],
                'fifty_two_week_high': info['fiftyTwoWeekHigh'],
                'fifty_day_average': info['fiftyDayAverage'],
                'fifty_two_week_change': info['52WeekChange'],
                'price_to_sales_trailing_12_months': info['priceToSalesTrailing12Months'],
                'profit_margin': info['profitMargins'],
                'trailing_eps': info['trailingEps'],
                'forward_eps': info['forwardEps'],
                'held_percent_insiders': info['heldPercentInsiders']

            }
        except KeyError as e:
            print(e)
    return json.dumps({"stocks": sorted_stocks})



def converter(obj):
    if isinstance(obj, Timestamp):
        return obj.__str__()


if __name__ == "__main__":
    app.run()
