import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm
print("\CONWAY's GAME OF LIFE")
a=np.zeros(shape=(102,102))
#Code segment for user input
#n=int(input(\"Enter no of 1's: \"))
#for i in range(n):
    #i=input(\"Enter index of 1's( 'FORMAT: 1,2' where x=1 y=2)\")
        #x=i.split(\",\")
            #s=int(x[0])
                #d=int(x[1])
                    #a[s][d]=1
#Code segment for static input
for i in range(45,55):
    a[55][i]=1
ite=0
list3=[]
list4=[]
list5=[]
list6=[]
#LOOP for evaluating CELLS start
while(ite<20):
    list3.clear()
    list4.clear()
    list5.clear()
    list6.clear()
    for i in range(1,101):
        for j in range(1,101):
            count=0
            if (a[i][j]==0):
                n=i
                m=j
                for n in range(i-1,i+2):
                    for m in range(j-1,j+2):
                        if a[n][m]==1:
                            count=count+1
                if(count==3):
                    list3.append(i)
                    list4.append(j)
            elif(a[i][j]==1):
                n=i
                m=j
                for n in range(i-1,i+2):
                    for m in range(j-1,j+2):
                        if a[n][m]==1:
                            count+=1
                if((count-1)<2 or (count-1)>3):
                    list5.append(i)
                    list6.append(j)
    for i in range(len(list3)):
        a[list3[i]][list4[i]]=1
    for i in range(len(list5)):
        a[list5[i]][list6[i]]=0
    ite=ite+1
#LOOP Ends after 20 iterations.
#CODE for changing the CELLS
list1=[]
list2=[]
for i in range(1,101):
    for j in range(1,101):
        if(a[i][j]==1):
            list1.append(i)
            list2.append(j)
            
# CODE for displaying output
fig, ax0 = plt.subplots()
c = ax0.pcolor(a,edgecolors='k',linewidths=1)
ax0.set_title("\Conway's GAME OF LIFE")
fig.tight_layout()
plt.show()