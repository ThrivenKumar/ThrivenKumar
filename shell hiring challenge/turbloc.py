import pandas as pd
import numpy as np
import math
import random
import csv
f=open("turbloc.csv","a+")
#f.truncate(0)
#f1=open("turbloc2.csv","a+")
#f.write("x,y\n")
#df = pd.read_csv('/Users/thrivenkumar/Desktop/turbloc.csv', sep=',')
#turb_coords = df.to_numpy(dtype = np.float32)
def randomnumber():
    x=random.randrange(50,3951)
    y=random.randrange(50,3951)
    return x,y
"""lx=list(turb_coords[:,0])
ly=list(turb_coords[:,1])
angle=list(range(0,360,10))
count=0
count2=0
while len(lx)<50:
    #count+=1
    #print("Iteration Number: ",count)
    x,y=randomnumber()
    boolis1=True
    #boolis2=True
    for k in range(len(lx)):
        val1=(lx[k]-x)**2
        val2=(ly[k]-y)**2
        val3=math.sqrt(val1+val2)
        if val3<400:
            boolis1=False
    if boolis1:
        lx.append(x)
        ly.append(y)
        f.write(str(x)+","+str(y)+"\n")
"""

"""
for i in range(10):
    x=x+433
    f.write(str(x)+","+str(y)+"\n")
"""
"""for i in range(9):
    x=x-400
    y=math.sqrt(1600*(x-50))+2000
    f.write(str(x)+","+str(y)+"\n")
"""
"""
for i in range(50,3900,400):
    x=i
    val2=math.sqrt(15207500-(100*x)-x**2)
    y=(val2/2)+2000
    f.write(str(x)+", "+str(y)+"\n")
    """
"""
for i in range(30):
    angle=5.91*(i+1)
    y=math.sin(math.radians(angle))*r
    y=y+50
    x=math.cos(math.radians(angle))*r
    x=x+2000
    f.write(str(x)+','+str(y)+"\n")
    #f.write(str(x)+","+str(y)+"\n")
    """
for i in range(1,10):
    x=572.5+math.cos(math.radians(30))*400*i
    y=2000+math.sin(math.radians(30))*400*i
    f.write(str(x)+","+str(y)+"\n")
for i in range(1,10):
    x=3950+math.cos(math.radians(150))*400*i
    y=50+math.sin(math.radians(150))*400*i
    f.write(str(x)+","+str(y)+"\n")
