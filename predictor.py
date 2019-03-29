"""
A .py file for the Predictor module. To execute this code, we will use the following command:
python3 predictor.py ticker info filename graph filename col t

– Define a function that takes the information file name, a ticker, a column name (say col which is either
  latestPrice or latestVolume), a time range, t and a graph file name as the input.

– The function is called by main, which accepts the arguments and passes those to the function.

– The function must read the data from the information file, select the data for the specified ticker, and
  train a machine learning based model to predict the value of the specified column for the next t minutes.

– You should only use the Time column (you can split it into hours and minutes) to predict the value of
  col based on the historical data stored in the information file.

– You must use the linear regression in sklearn.linear model to train using the historical data for the
  specific ticker stored in the information file and then predict the result for the next t minutes.

– You must also plot and save the plot for the historical variation in the value of col as well as the predicted
  values. The actual and predicted data should be plotted out on the same graph in two different colours.

Mehran will work on this
"""
import sys
import csv
import matplotlib.pyplot as plt
import datetime
import numpy as np
from sklearn.linear_model import LinearRegression

labels = ['time', 'ticker', 'latestPrice', 'latestVolume', 'close', 'open', 'low', 'high']


def buildListofTickerDictionaries(csv_filename, ticker, col_name):
    dict_list = []
    with open(csv_filename) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if ticker in row:
                ticker_dictionary = dict()
                for i in range(len(row)):
                    if labels[i] == col_name or labels[i] == "time" or labels[i] == "ticker":
                        ticker_dictionary[labels[i]] = row[i]

                dict_list.append(ticker_dictionary)

    return dict_list


def predict(ticker, csv_filename,  graph_filename, col_name, time_range):
    dict_list = buildListofTickerDictionaries(csv_filename, ticker, col_name)
    for ticker_dictionary in dict_list:
        Time = ticker_dictionary.get("time").split(":")
        ticker_dictionary["hour"] = Time[0]
        ticker_dictionary["minute"] = Time[1]

    # Populate two arrays of known data
    x_time_list = []
    y_value_list = []
    for ticker_dictionary in dict_list:
        x_time_list.append(int(ticker_dictionary.get("hour"))*60 + int(ticker_dictionary.get("minute")))
        y_value_list.append(float(ticker_dictionary.get(col_name)))

    # Create line of fit
    regr = LinearRegression()
    np_x_time_list = np.array(x_time_list).reshape(-1, 1)
    np_y_value_list = np.array(y_value_list)
    regr.fit(np_x_time_list, np_y_value_list)

    # Create an array of minutes to predict
    minutes_to_predict = []
    now = datetime.datetime.now()
    for i in range(0, int(time_range) + 1):
        minutes_to_predict.append(now.hour*60 + now.minute + i)

    # Create prediction
    np_minutes_to_predict = np.array(minutes_to_predict).reshape(-1, 1)
    prediction = regr.predict(np_minutes_to_predict)

    plt.title(ticker)
    plt.ylabel(col_name)
    plt.xlabel("Time (minutes)")
    plt.scatter(x_time_list, y_value_list, color='blue')
    plt.scatter(minutes_to_predict, prediction, color='red')
    plt.savefig(graph_filename)


if __name__ == "__main__":
    predict(ticker=sys.argv[1], csv_filename=sys.argv[2], graph_filename=sys.argv[3], col_name=sys.argv[4], time_range=sys.argv[5])
