import numpy as np
def Aggrigates():
    #sum
    #Syntax: numpy.sum(arr, axis, dtype, out): 
    #the axis value 1 sums up the row
    #the axis value 0 sums up the column(initial)
    x=np.array([[1,2,3],[3,2,5]])
    y=np.array([[2,2,1],[1,2,4]])

    #summing up the row 
    z=np.sum((x,y),axis=0)
    print(z)
#Aggrigates()

#