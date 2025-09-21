#using numpy
import numpy as np

#text=np.loadtxt('homeData.csv',delimiter=",",encoding='UTF-8',skiprows=0,dtype=str)

#another method

text=np.genfromtxt('homeData.csv',delimiter=',',dtype=str,skip_header=1)
print(text)