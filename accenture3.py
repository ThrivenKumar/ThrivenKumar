n=int(input())
points=input().split()
list1=[]
for i in points:
    list1.append(int(i))
slope=0
booli=False
for i in range(0,n,2):
    numer=list1[i+3]-list1[i+1]
    denom=list1[i+2]-list1[i]
    sl=numer/denom
    if i>0:
        if slope!=sl:
            booli=True
            break
    slope=sl
if booli==False:
    const=list1[1]-(slope*list1[0])
    print("1y+"+str(slope)+"x="+str(const))
else:
    print(0)
