def func(maxTravelDist,forwardRouteList,returnRouteList):
    list1=[]
    maxi=-1
    for i in range(len(forwardRouteList)):
        for j in range(len(returnRouteList)):
            count=forwardRouteList[i][1]+returnRouteList[j][1]
            if count<=maxTravelDist and count>=maxi:
                maxi=count
    if maxi==-1:
        return [()]
    for i in range(len(forwardRouteList)):
        for j in range(len(returnRouteList)):
            count=forwardRouteList[i][1]+returnRouteList[j][1]
            if count==maxi:
                list1.append([forwardRouteList[i][0],returnRouteList[j][0]])
    
    return list1

print(func(20,[[1, 8], [2, 7], [3, 14]],[[1, 5], [2, 10], [3, 14]]))
                
20 [[1, 8], [2, 7], [3, 14]] [[1, 5], [2, 10], [3, 14]]
6 [[1, 3], [2, 5], [3, 7], [4, 10]] [[1, 2], [2, 3], [3, 4], [4, 5]]
62 [[1, 30], [2, 70], [3, 50], [4, 100]] [[1, 30], [2, 40], [3, 50], [4, 20]]
20 [[1, 8], [2, 7], [3, 14]] [[1, 5], [2, 10], [3, 14]]
6 [[1, 3], [2, 5], [3, 7], [4, 10]] [[1, 2], [2, 3], [3, 4], [4, 5]]
19 [[1, 10], [3, 12], [4, 14], [2, 13]] [[1, 7], [2, 6], [3, 10]]






