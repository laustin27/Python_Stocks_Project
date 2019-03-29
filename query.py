"""
A .py file for the Query module. To execute this, the command used will be:
python3 query.py –verbose True/False –file info filename –ticker ticker –time time The time format should
be HH:MM. Example is: 13:31.

-Define a function that takes the information file name, time and the ticker as the input and prints the
  details corresponding to a specific time and ticker symbol to the terminal. The data must be printed as
  follows:
             field 1: value 1
             field 2: value 2
             .
             .
             .
             field n: value n

– The above function also takes a verbose flag, which when true, the number of rows and number of
  columns in the information file will be printed out as well as the names of the columns.

– Should have a main that takes the following flags and calls the function to print the values:
             verbose
             time (HH:MM format)
             file (information file that contains the information)
             ticker
"""




import sys
import csv

labels = ['Time', 'Ticker', 'latestPrice', 'latestVolume', 'Close', 'Open', 'low', 'high']


def readData(verbose, filename, ticker, time):
    ticker_dictionary = dict()
    with open(filename) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if time in row and ticker in row:
                if verbose:
                    print("# of columns", len(row))
                    row_count = sum(1 for row in readCSV)
                    print("# of rows", row_count)
                print("File", filename)
                for i in range(len(row)):
                    ticker_dictionary[labels[i]] = row[i]
                    print(f'{labels[i]}: {row[i]}')



    return ticker_dictionary


if __name__ == "__main__":
    if(len(sys.argv)!=9):
        print(f'number of parameters provided is {len(sys.argv)}! It should be 9!')
    else:
        readData(verbose=sys.argv[2], filename=sys.argv[4], ticker=sys.argv[6], time=sys.argv[8])
