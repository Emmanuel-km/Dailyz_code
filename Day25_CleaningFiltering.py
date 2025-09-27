import pandas as pd

df=pd.read_csv('homeData.csv')

print(df['barometric_pressure'].mean)

print(df['barometric_pressure'].max)