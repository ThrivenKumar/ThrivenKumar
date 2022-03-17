def ReplaceWithCoprime(arr):
    count1=0
    for i in arr:
        list1=[]
        coprime="No CoPrime"
        for j in range(2,(i//2)+1):
            if i%j==0:
                list1.append(j)
        for j in range(250,i,-1):
            count=0
            for k in list1:
                if j%k==0:
                    count=1
            if count==0:
                coprime1=j
                break
        for j in range(2,i):
            count=0
            for k in list1:
                if j%k==0:
                    count=1
            if count==0:
                coprime2=j
                break
        if (coprime1-i)>(i-coprime2):
            coprime=coprime1
        else:
            coprime=coprime2
        arr[count1]=coprime
        count1=count1+1
    return arr
print(ReplaceWithCoprime([60,246,75,103,155,110]))
