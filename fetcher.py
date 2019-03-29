"""
A .py file for the Fetcher module. To execute this code, we will use the following command:
python3 fetcher.py time lim ticker filename info filename
-QUERY EVERY MINUTE

- Read all the tickers from an input file (tickers.txt). The tickers are listed one per line.

– Define a function that updates the current stock information for the ticker that is passed as an argument.
  The information is written and updated in an information file (say info.csv for example).

– The module should call this function for each input ticker in tickers.txt file.

– This module should run for specified time period, say time lim in seconds and update the data in the
  information file.

– The information file should be a csv file, with the first row being the column headers. For each ticker in
  the tickers.txt file, the information file, should have one row for each minute.

– The Time column should contain time in the HH:MM format with HH ranging from 00 to 23. There
  should be one and only one row corresponding a specific value of Time and Ticker.

– In order to extract the stock information for a ticker, say ”AAPL”, you should use the iex-api-python
  which is described here: https://pypi.org/project/iex-api-python/. You need to fetch the current data for the following fields: low, high, open, close, latestPrice, latestVolume. Use the
  quote() function of the Stock corresponding to the ticker.

– The csv must have data in the format:
  Time, Ticker, latestPrice, latestVolume, Close, Open, low, high

– Store the time of the query and the respective keys and values in the info.txt file. For each iteration,
  during which you save the data for a specific minute, you may wait till the start of the next minute, say,
  12:37 and then save the data for all tickers during that iteration with the Time field set to the minute
  (12:37).

– Please use the information on the API page to figure out how to install iex-api-python. The page also
  has the information for fetching necessary data about a stock ticker.

– The arguments passed to this module are: time lim, ticker filename, info filename
"""

import sys
import csv
import datetime
import time
from iex import Stock


def writeToFile(ticker, info_writer, endTime):
    currentDT = datetime.datetime.now()
    hour = str(currentDT.hour)
    minute = currentDT.minute
    if minute < 10:
        minute = '0' + str(minute)
    else:
        minute = str(minute)

    # If function exceeds its endTime then exit the module
    if currentDT >= endTime:
        return

    ticker_info = Stock(symbol=ticker).quote()
    info_writer.writerow([hour + ':' + minute, ticker, ticker_info['low'], ticker_info['high'], ticker_info['open'],
                          ticker_info['close'], ticker_info['latestPrice'], ticker_info['latestVolume']])


def readTickers(time_lim, ticker_file, csv_file):
    open_csv = open(csv_file, 'a')
    info_writer = csv.writer(open_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    while True:
        fp = open(ticker_file)
        # Calculate time to sleep until next minute starts
        sleepTime = 60 - (datetime.datetime.now().second + datetime.datetime.now().microsecond / 1000000.0)
        time.sleep(sleepTime)

        # Calculate how long the function should run
        endTime = datetime.datetime.now() + datetime.timedelta(seconds=int(time_lim))
        for ticker in fp:
            writeToFile(ticker=ticker.strip('\n'), info_writer=info_writer, endTime=endTime)
        fp.close()


if __name__ == "__main__":
    readTickers(time_lim=sys.argv[1], ticker_file=sys.argv[2], csv_file=sys.argv[3])
