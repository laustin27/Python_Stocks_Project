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
labels=['Time', 'Ticker', 'latestPrice', 'latestVolume', 'Close', 'Open', 'low', 'high']
def readData(verbose, filename, ticker, time):
    with open(filename, 'r') as info:
        for line in info:
            if((time+', '+ticker) in line):
                tokens = line.strip().split()
                for i in range(len(tokens)):
                    print(f'{labels[i]}: {tokens[i]}'.replace(',',''))





if __name__ == "__main__":
    if(len(sys.argv)!=9):
        print(f'number of parameters provided is {len(sys.argv)}! It should be 9!')
    else:
        readData(sys.argv[2], sys.argv[4], sys.argv[6], sys.argv[8])
