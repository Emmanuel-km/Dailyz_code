#These are imports necessary for visualization

import seaborn as sns
import pandas as pd 
import matplotlib.pyplot as plt

# Data extraction and cleaning
"""
 in this case the home data CSV 
 file will be looked upon and 
 operations on data will  be handled by
 pandas
"""

df=pd.read_csv('homeData.csv')
#droping null values
df.dropna(inplace=True)
#data
data=df[['wind_speed','time']]
