import numpy as np
import matplotlib.pyplot as plt

cvalues=[20.1,20.7,23.1,22.6,24.5,25.3,22.0,20.4,21.9]

C=np.array(cvalues)

#%matplotlib inline-making juypter not create a new window
def showploting():
    plt.plot(C)
    plt.show()
#showploting()

x=np.arange(0,40,4)
#print(x)
 
x=np.arange(10.4)
#print(x)

x=np.linspace(0,40,num=11,endpoint=True,retstep=True)
#print(x)

x=np.array(78)
#print(x)
#print(np.ndim(x))

x=np.array([3,5,7,8,9,1,2])

x=np.array([[3,6,9,12,15,18,21,24,27,30],[9,18,27,36,45,54,63,72,81,90]])
#print(x)

x=np.array([[[2,4,6],[1,2,3]],[[3,6,9],[6,12,18]],[[4,8,12],[8,16,24]]])
print(x)