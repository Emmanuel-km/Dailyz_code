#in this section we will look at handling data
# with pandas for convinience

#importing pandas and csv
import csv

import pandas

#storing the contents of csv files in varible enhanced by pandas

data=pandas.read_csv('NarokSolarMeasurements.csv')

#looping columns in the data
#filter
data.head(12)
#for col in data:
    print(col)
