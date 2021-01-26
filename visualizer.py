import pandas as pd 
from mpl_toolkits.mplot3d import axes3d
from matplotlib import pyplot as plt 


df = pd.read_csv('final_data.csv')

print(df.shape)

fig = plt.figure()
ax = plt.axes(projection="3d")

# Plotting
r = df['red']
g = df['green']
b = df['blue']


ax.scatter3D(r,g,b)
ax.scatter3D(255, 255, 255, label='White')
ax.scatter3D(0, 0, 0, label='Black')




#Labeling
ax.set_xlabel('R')
ax.set_ylabel('G')
ax.set_zlabel('B')
plt.legend()
plt.show()