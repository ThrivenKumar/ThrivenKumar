import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
def Colorvalue(i):
    if(i%13==0):
        color='m'
    elif(i%13==1):
        color='g'
    elif(i%13==2):
        color='r'
    elif(i%13==3):
        color='c'
    elif(i%13==4):
        color='b'
    elif(i%13==5):
        color='y'
    elif(i%13==6):
        color='k'
    elif(i%13==7):
        color='#fc8c03'
    elif(i%13==8):
        color='#8403fc'
    elif(i%13==9):
        color='#6b7a91'
    elif(i%13==10):
        color='#9c6571'
    elif(i%13==11):
        color='#856100'
    elif(i%13==12):
        color='#90659c'
    return color

df = pd.read_csv('/Users/thrivenkumar/Desktop/turbloc.csv', sep=',')
turb_coords = df.to_numpy(dtype = np.float32)
x=turb_coords[:,0]
y=turb_coords[:,1]
fig, ax=plt.subplots()
ax.scatter(x, y, color= "green",marker= ".", s=30)
ax.set(xlim=(0, 4000), ylim = (0, 4000))
for i in range(50):
    x1=np.linspace(x[i],4000)
    y1=0.05*x1+(y[i]+50-0.05*x[i])
    ax.plot(x1,y1, Colorvalue(i),linewidth=1.0,linestyle="dashed")
    y1=-0.05*x1+(y[i]-50+0.05*x[i])
    ax.plot(x1,y1,Colorvalue(i),linewidth=1.0,linestyle="dashed")
# x-axis label
plt.xlabel('x - axis')
# frequency label
plt.ylabel('y - axis')
# plot title
plt.title('My scatter plot!')
# showing legend
plt.legend()
# function to show the plot
plt.show()
