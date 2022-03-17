def ascendingOrder(N,A):
    index1=0
    index2=0
    length=[]
    count=0
    for i in range(N-1):
        print(i)
        if A[i]<A[i+1]:
            count+=1
        else:
            length.append(count)
            count=0
    count=max(length)
    print(length)
    return N-(count+1)
