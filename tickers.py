"""
A .py file for the Tickers module. To execute this code, we will use the following command:
python3 tickers.py number of tickers ticker filename

– Have a function, say save tickers that fetches the first n valid tickers from the following URL and
  writes the tickers in a file, say tickers.txt:
  http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQrender=download

– To ensure that a ticker is valid, you should use the iex-api-python to verify that the price function
  for the Stock corresponding to the fetched ticker works. That is, if there are some tickers for which the
  price() function of the iex API does not work, then that ticker should not be written to the file.

– Write one ticker symbol per line of the file tickers.txt.

– The number n will be provided as a system argument to the module. There should be a main module
  that calls the save tickers function and passes the value of n to it. The value of n will be ≤ 150.
"""
import sys
import requests
from pyquery import PyQuery
from iex import Stock


def saveTickers(n, filename):
    """
    fetch the first n valid tickers from http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQrender=download
    and writes the tickers in a file that is returned
    :return:

    """
    if int(n) > 150:
        raise Exception("You need to give me a number less than or equal to 150!")

    request = requests.get("https://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&pagesize=" + n)
    parser = PyQuery(request.text)
    table = parser("#CompanylistResults")

    table_parser = PyQuery(table)
    symbols = table_parser("h3")
    symbol_list = [symbol for symbol in symbols.text().split()]

    for ticker in symbol_list:
        try:
            Stock(ticker).price()
        except:
            symbol_list.remove(ticker)

    f = open(filename, "w")
    for symbol in symbol_list:
        f.write(symbol + '\n')

    f.close()


if __name__ == "__main__":
    saveTickers(sys.argv[1], sys.argv[2])

