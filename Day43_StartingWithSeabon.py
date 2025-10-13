from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
import seaborn as sb
import pandas as pd

#sns.barplot(x="Category", y="Values", data=df, palette="viridis")

#fig,ax=plt.subplots(2,2)
sb.set_style("whitegrid")
sb.set()
sb.despine()
y=np.random.random(7)+2
y[0]=0
x=np.arange(1,8)
plt.plot(x,y)
'''
ax[0,1].plot(x,y)
ax[0,1].plot(sb.set_context('poster'))
'''
#sub context values = paper, notebook, talk, poster
sb.set_context('paper')


plt.xlabel('Days')
plt.ylabel('deviation in temperature')
plt.title('plot of deviation in temperature in\n Week 38 2025')
plt.show()