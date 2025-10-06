import matplotlib.pyplot as plt
import numpy as np

x=np.random.random(7)
x=x+2
#x=np.linspace(1,7,num=7,endpoint=True)
y=np.arange(1,8)

plt.plot(y,x)
plt.xlabel('Days')
plt.ylabel('deviation in temperature')

#giving the title
plt.title('plot of deviation in temperature in\n Week 38 2025')

plt.legend()
plt.show()