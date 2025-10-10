import matplotlib.pyplot as plt

power=['solar','wind','hydropower']
sizes=[62,17,18]
explode=[0.2,0,0]

fig,ax=plt.subplots()
ax.pie(sizes, explode=explode, labels=power, autopct='%1.1f%%',shadow=True, startangle=90)
ax.axis('equal')

plt.title('proportion of power generated')
plt.show()