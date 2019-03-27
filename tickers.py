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
from selenium import webdriver


def pull150ItemsURL():
    # Set up Chrome instance of this url
    driver = webdriver.Chrome(executable_path='./chromedriver')
    driver.get('http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQrender=download')

    # Click on the 150 option in page size select so we can get all the symbols we need
    page_size_select = driver.find_element_by_id('main_content_lstpagesize')
    for page_size_option in page_size_select.find_elements_by_tag_name('option'):
        if page_size_option.text == '150 Items Per Page':
            page_size_option.click()
            break

    return driver.current_url


def saveTickers(n, filename):
    if int(n) > 150:
        raise Exception("You need to give me a number less than or equal to 150!")

    # Create request with 150 item url
    request = requests.get(url=pull150ItemsURL())
    parser = PyQuery(request.text)
    table = parser("#CompanylistResults")

    table_parser = PyQuery(table)
    symbols = table_parser("h3")
    symbol_list = [symbol for symbol in symbols.text().split()]

    for ticker in symbol_list:
        try:
            Stock(symbol=ticker).price()
        except:
            symbol_list.remove(ticker)

    f = open(filename, "w")
    for symbol in symbol_list:
        f.write(symbol + '\n')

    f.close()


if __name__ == "__main__":
    saveTickers(n=sys.argv[1], filename=sys.argv[2])

