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
