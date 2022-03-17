def SpiralTraverse(arr):
    list1=[]
    elementsTraversed=0
    m=len(arr)
    n=len(arr[0])
    start1=0
    end1=m-1
    start2=0
    end2=n-1
    while elementsTraversed<(m*n):
        j=start2
        for i in range(start1,end1+1):
            list1.append(arr[j][i])
            elementsTraversed+=1
        i=end1
        for j in range(start2+1,end2):
            list1.append(arr[j][i])
            elementsTraversed+=1
        j=end2
        for i in range(end1,start1-1,-1):
            list1.append(arr[j][i])
            elementsTraversed+=1
        i=start1
        for j in range(end2-1,start2,-1):
            list1.append(arr[j][i])
            elementsTraversed+=1
        start1+=1
        end1-=1
        start2+=1
        end2-=1
    return list1
print(SpiralTraverse([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))
