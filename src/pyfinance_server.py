# pyfinance_server.py

from flask import Flask
import yfinance as yf
import json
from pandas import Timestamp

app = Flask(__name__)


@app.route("/tickers/<string:ticker>/info")
def info(ticker):
    return yf.Ticker(ticker).info


@app.route("/tickers/<string:ticker>/institutional-holders")
def institutional_holders(ticker):
    response = yf.Ticker(ticker).institutional_holders
    return response.to_json()


@app.route("/tickers/<string:ticker>/actions")
def actions(ticker):
    response = yf.Ticker(ticker).actions
    return response.to_json()


@app.route("/tickers/<string:ticker>/dividends")
def dividends(ticker):
    response = yf.Ticker(ticker).dividends
    return response.to_json()


@app.route("/tickers/<string:ticker>/splits")
def splits(ticker):
    response = yf.Ticker(ticker).splits
    return response.to_json()


@app.route("/tickers/<string:ticker>/major-holders")
def major_holders(ticker):
    response = yf.Ticker(ticker).major_holders
    return response.to_json()


@app.route("/tickers/<string:ticker>/cashflow")
def cashflow(ticker):
    response = yf.Ticker(ticker).cashflow
    return response.to_json()


@app.route("/tickers/<string:ticker>/quarterly-cashflow")
def quarterly_cashflow(ticker):
    response = yf.Ticker(ticker).quarterly_cashflow
    return response.to_json()


@app.route("/tickers/<string:ticker>/earnings")
def earnings(ticker):
    response = yf.Ticker(ticker).earnings
    return response.to_json()


@app.route("/tickers/<string:ticker>/quarterly-earnings")
def quarterly_earnings(ticker):
    response = yf.Ticker(ticker).quarterly_earnings
    return response.to_json()


@app.route("/tickers/<string:ticker>/sustainability")
def sustainability(ticker):
    response = yf.Ticker(ticker).sustainability
    return response.to_json()


@app.route("/tickers/<string:ticker>/recommendations")
def recommendations(ticker):
    response = yf.Ticker(ticker).recommendations
    response.reset_index(drop=True, inplace=True)
    return response.to_json()


@app.route("/tickers/<string:ticker>/calendar")
def calendar(ticker):
    response = yf.Ticker(ticker).calendar
    return response.to_json()


@app.route("/tickers/<string:ticker>/isin")
def isin(ticker):
    response = {"isin": yf.Ticker(ticker).isin}
    return response


@app.route("/tickers/<string:ticker>/options")
def options(ticker):
    response = {"options": list(yf.Ticker(ticker).options)}
    return response


def converter(obj):
    if isinstance(obj, Timestamp):
        return obj.__str__()


if __name__ == "__main__":
    app.run()
