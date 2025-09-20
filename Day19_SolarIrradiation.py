#working with solar data 
#opening csv files cleaning, computing monthly average over 
#the past 30 years monthly
#summerizing the data

#opening csv files
#csv files are commer separated values

#so first;

import csv
import numpy as np
with open('NarokSolarMeasurements.csv','r+') as file:
    #using the dict reader to find the relative_humidity
    #csvreader=csv.DictReader(file)

    #for coninient data handling lets use the normal
    csvreader=csv.reader(file)

    #for skipping the first row
    next(csvreader)
    count=0
    
    value=np.array([])
    for i in csvreader:

        i=float(i[5])
        
        #print(i["relative_humidity"])
        #handling the file in a numpy array
        
        #conveting the string value into float
        #try catch block for coviniece
        try:
            value=np.append(value,i)
            count+=1
        except:
            print("an error has been found")
            continue   
    z=np.sum(value)
    print(z)