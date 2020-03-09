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
    response = yf.Ticker(ticker).institutional_holders.values.tolist()
    response_dict = {"institutional_holders": response}
    return json.dumps(response_dict, default=converter)


def converter(obj):
    if isinstance(obj, Timestamp):
        return obj.__str__()


if __name__ == "__main__":
    app.run()
