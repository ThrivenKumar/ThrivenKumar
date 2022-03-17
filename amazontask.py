def smo(parcels,k):
    parcels.sort()
    newpackcount=k-len(parcels)
    mini=min(parcels)
    maxi=max(parcels)
    print(parcels,newpackcount,mini,maxi)
    sums=0
    if mini-1>1:
        if newpackcount>mini-1:
            sums+=sum(range(1,mini))
            newpackcount-=mini-1
            print("First",sums,newpackcount)
        else:
            sums+=sum(range(1,newpackcount+1))
            newpackcount=0
            print("First",sums,newpackcount)
    if newpackcount>0:
        for i in range(len(parcels)-1):
            temp=parcels[i+1]-parcels[i]
            if temp>1:
                if newpackcount>=temp:
                    sums+=sum(range(parcels[i]+1,parcels[i+1]))
                    newpackcount-=temp-1
                    print("Second",sums,newpackcount,temp)
                else:
                    sums+=sum(range(parcels[i]+1,parcels[i]+newpackcount+1))
                    newpackcount=0
                    print("Thrid",sums,newpackcount,temp)

    i=maxi+1
    while newpackcount>0:
        sums+=i
        newpackcount-=1
    print("Fourth",sums,newpackcount)
    return sums

print(smo([3,4,1,5,6],7))