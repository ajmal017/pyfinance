import yfinance as yf

msft = yf.Ticker("MSFT")

file = open("./source_files/nasdaqlisted.txt")
print(file.readline())

