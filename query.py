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
