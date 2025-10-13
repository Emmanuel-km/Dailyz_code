import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
''' improving codes by days'''


MONTH=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
MLY_PRCP_NORMAL=np.random.randint(0,8,12)
MLY_PRCP_25PCTL=(MLY_PRCP_NORMAL*0.25)
MLY_PRCP_75PCTL=MLY_PRCP_NORMAL*1.75


MLY_PRCP_NORMAL1=np.random.randint(0,8,12)
MLY_PRCP_25PCTL1=(MLY_PRCP_NORMAL*0.25)
MLY_PRCP_75PCTL1=MLY_PRCP_NORMAL*1.75



me={"MONTH":MONTH,"MLY-PRCP-NORMAL":MLY_PRCP_NORMAL,'MLY-PRCP-75PCTL':MLY_PRCP_75PCTL,'MLY-PRCP-25PCTL':MLY_PRCP_75PCTL}
me2={"MONTH":MONTH,"MLY-PRCP-NORMAL":MLY_PRCP_NORMAL1,'MLY-PRCP-75PCTL':MLY_PRCP_75PCTL1,'MLY-PRCP-25PCTL':MLY_PRCP_75PCTL1}

#seattle_weather=pd.DataFrame((MONTH,MLY_PRCP_NORMAL,MLY_PRCP_75PCTL,MLY_PRCP_25PCTL))
seattle_weather=pd.DataFrame(me)
austin_weather=pd.DataFrame(me2)
# Create a figure and an array of axes: 2 rows, 1 column with shared y axis
fig, ax = plt.subplots(2, 1, sharey=True)

# Plot Seattle precipitation data in the top axes
ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"], color = 'b')
ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-25PCTL"], color = 'm', linestyle='--')
ax[0].plot(seattle_weather["MONTH"],seattle_weather["MLY-PRCP-75PCTL"], color = 'g',  marker='^')

# Plot Austin precipitation data in the bottom axes
ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"], color = 'r')
ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-25PCTL"], color = 'm', marker='v')
ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-75PCTL"], color = 'g', marker='^')

plt.show()