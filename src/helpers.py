def get_tickers():
    ticker_method = lambda stock: stock.pop(0)
    watch_filter_method = lambda stock: stock.pop(-1) == 'Y'
    split_stock_line = lambda line: line.strip().split('|')
    with open('../source_files/nasdaqlisted.txt') as nasdaq:
        nasdaq_lines = list(map(ticker_method, filter(watch_filter_method, map(split_stock_line, nasdaq.readlines()))))
    with open('../source_files/otherlisted.txt') as other:
        other_lines = list(map(ticker_method, filter(watch_filter_method, map(split_stock_line, other.readlines()))))
    return nasdaq_lines + other_lines
