import numpy as np
import matplotlib.pyplot as plt

cvalues=[20.1,20.7,23.1,22.6,24.5,25.3,22.0,20.4,21.9]

C=np.array(cvalues)

#%matplotlib inline-making juypter not create a new window
def showploting():
    plt.plot(C)
    plt.show()
#showploting()



