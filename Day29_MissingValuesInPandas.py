'''
this file is detection file where it 
detect wheather a file has null values 

so logging will be imported if dataframe has null values,
 it will send a critical message to the log file
'''
import pandas as pd
import numpy as np
import logging

file='NarokSolarMeasurements.csv'

df=pd.read_csv(file)
y=df[['air_temperature']]
LIST=np.array(y)


#print(isnull)
for i in LIST:
    if i == 'NaN':
    #setting up the the logging
    #basic logging example
     import logging
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%d-%m-%Y %H:%M:%S",
        filename="basic.log")
    logging.critical(f"The file [{file}] has null values ")