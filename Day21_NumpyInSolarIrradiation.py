#using numpy
import numpy as np

#text=np.loadtxt('homeData.csv',delimiter=',')

text=np.genfromtxt('homeData.csv',delimiter=',')
print(text)