# Python_Stocks_Project
Working with stocks data. Using the iex-api-python which is described here: https://pypi.org/project/iex-api-python/

## Tickers: 

 - Have a function, say **save tickers** that fetches the first n valid tickers from the following URL and writes the tickers in a file, say tickers.txt:
http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQrender=download


- To ensure that a ticker is valid, you should use the iex-api-python to verify that the price function for the Stock corresponding to the fetched ticker works. That is, if there are some tickers for which the **price()** function of the iex API does not work, then that ticker should not be written to the file.


- Write one ticker symbol per line of the file tickers.txt.


 - The number n will be provided as a system argument to the module. There should be a main module that calls the save tickers function and passes the value of n to it. The value of n will be ≤ 150.


---
## Fetcher:
- Read all the tickers from an input file (tickers.txt). The tickers are listed one per line.


- Define a function that updates the current stock information for the ticker that is passed as an argument. The information is written and updated in an information file (say info.csv for example).


- The module should call this function for each input ticker in tickers.txt file.


- This module should run for specified time period, say time lim in seconds and update the data in the information file.


- The information file should be a csv file, with the first row being the column headers. For each ticker in the tickers.txt file, the information file, should have one row for each minute.


- The Time column should contain time in the HH:MM format with HH ranging from 00 to 23. There should be one and only one row corresponding a specific value of Time and Ticker.


- In order to extract the stock information for a ticker, say ”AAPL”, you should use the iex-api-python which is described here: https://pypi.org/project/iex-api-python/.
You need to fetch the current data for the following fields: *low*, *high*, *open*, *close*, *latestPrice*, *latestVolume*. 
Use the **quote()** function of the Stock corresponding to the ticker.


- The csv must have data in the format:
   - *Time*, *Ticker*, *latestPrice*, *latestVolume*, *Close*, *Open*, *low*, *high*


- Store the time of the query and the respective keys and values in the info.txt file. For each iteration, during which you save the data for a specific minute, you may wait till the start of the next minute, say, 12:37 and then save the data for all tickers during that iteration with the Time field set to the minute (12:37).


- Please use the information on the API page to figure out how to install iex-api-python. The page also has the information for fetching necessary data about a stock ticker.


- The arguments passed to this module are: 
  - *time lim*
  - *ticker filename*
  - *info filename*


---
## Query:
- Define a function that takes the information file name, time and the ticker as the input and prints the details corresponding to a specific time and ticker symbol to the terminal. The data must be printed as follows:
>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;field 1: value 1


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;field 2: value 2


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;field n: value n


  - The above function also takes a verbose flag, which when true, the number of rows and number of columns in the information file will be printed out as well as the names of the columns.


  - Should have a main that takes the following flags and calls the function to print the values:
 >
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*verbose*


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*time* (HH:MM format)


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*file* (information file that contains the information)


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*ticker*



---
## Predictor:
- Define a function that takes the information file name, a ticker, a column name (say col which is either *latestPrice* or *latestVolume*), a time range, *t*, and a graph file name as the input.


- The function is called by main, which accepts the arguments and passes those to the function.


- The function must read the data from the information file, select the data for the specified ticker, and train a machine learning based model to predict the value of the specified column for the next t minutes.


- You should only use the Time column (you can split it into hours and minutes) to predict the value of col based on the historical data stored in the information file.


- You must use the linear regression in sklearn.linear model to train using the historical data for the specific ticker stored in the information file and then predict the result for the next t minutes.


- You must also plot and save the plot for the historical variation in the value of col as well as the predicted values. The actual and predicted data should be plotted out on the same graph in two different colours.
