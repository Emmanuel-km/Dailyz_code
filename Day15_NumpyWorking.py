import numpy as np
#so numpy generally is a library in python for holding 
#values in terms of arrays and working with them well
#so fast in accessing the contents inside arrays over lists

#creating an array in numpy
#types of arrays in numpy

#zero dimension
arr0=np.array(6)


#one dimension
arr1=np.array([26])
arr2=np.array([19,33,50,71])

#two-dimension
arr3=np.array([[1,3,5,7],[2,4,6,8]])


#three-dimension
#these are specialised two dimension
arr4=np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])

#checking number of dimension of each array
'''
print(arr0.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)
print(arr4.ndim)

'''

#creating arrays using arange
arr5=np.arange(0,50,8,dtype=float)

#creating arrays using linespace
#advantage is that you can perform many task with this
arr6=np.linspace(0,85,num=13,endpoint=True,retstep=True,dtype=float)

#performing under special arrays
#zero arrays
arr7=np.zeros((2,3),dtype=int,order='C')

#ones arrays
arr8=np.ones((2,4),dtype=float,order='F')

#eye arrays
arr9=np.eye(3,3,0,dtype=int,order='F')

#Random arrays
from numpy import random

arr10=random.randint(3,45,(2,3))

#random from a choice
arr11=random.choice([6,7,11,9,0,98,75,41,23,56,78],size=(2,3))


