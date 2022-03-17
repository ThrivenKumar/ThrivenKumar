def somefunc(N,A):
    list1=[]
    for i in range(N):
        mindiff=max(A)-min(A)
        maxdiff=min(A)-max(A)
        nearestmini=0
        nearestmaxi=0
        for j in range(N):
            diff=A[i]-A[j]
            if diff<mindiff and diff>0:
                mindiff=diff
                nearestmini=A[j]
            if diff>maxdiff and diff<0:
                maxdiff=diff
                nearestmaxi=A[j]
        list1.append(nearestmini+nearestmaxi)
    return list1
print(somefunc(5,[1,5,2,3,8]))
