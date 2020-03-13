from flask import Flask
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
            yf.Ticker(t).to_json()
        except HTTPError:
            pass

    num_cores = multiprocessing.cpu_count()
    response = Parallel(n_jobs=num_cores)(delayed(run)(t) for t in tqdm(get_tickers()))

    return json.dumps({"stocks": response})


def converter(obj):
    if isinstance(obj, Timestamp):
        return obj.__str__()


if __name__ == "__main__":
    app.run()
