import numpy as np
import matplotlib.pyplot as plt

solar_radiation=x=np.random.randint(low=21,high=45,size=6)
months=['January','February','March','April','May','June']


x=np.random.random(7)
x=x+2
#x=np.linspace(1,7,num=7,endpoint=True)
y=np.arange(1,8)


plt.style.use('ggplot')
plt.plot(x,linestyle=':',linewidth=2)
plt.show()