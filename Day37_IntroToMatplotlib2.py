import numpy as np
import matplotlib.pyplot as plt

solar_radiation=x=np.random.randint(low=21,high=45,size=6)
months=['January','February','March','April','May','June']

plt.suptitle("two graphs in one")
plt.subplot(2,1,1)
plt.bar(months,solar_radiation,color='maroon')
plt.title('solar radiation intensity \n(by the second quater of year 2025)')
plt.xlabel('months')
plt.ylabel('solar radiation average')
plt.plot(scaley=True,scalex=True)


#scatter diagram
high_temperature=np.random.randint(low=22,high=36,size=31)
low_temperature=np.random.randint(low=14,high=26,size=31)

plt.subplot(2,1,2)
plt.scatter(high_temperature,low_temperature,color='yellow')
plt.title('variation in temperature')
plt.xlabel('high temperaatue')
plt.ylabel('low temperature')
plt.plot()
#plt.legend()
plt.show()



''' 
future self...

this code above has only one thing left to do and that is
scaling up the subloplot to make harmonised good graph
'''