def func(deviceCapacity,list1,list2):
    list3=[]
    list4=[]
    maxi=0
    maxi2=0
    for i in range(len(list1)):
        if maxi>maxi2:
            list4.clear()
            list4.extend(list3)
        for j in range(len(list2)):
            count=list1[i][1]+list2[j][1]
            if count==maxi:
                list3.append([list1[i][0],list2[j][0]])
            if count>maxi and count<=deviceCapacity:
                maxi=count
                list3.clear()
                list3.append([list1[i][0],list2[j][0]])
    return list4

print(func(7,[[1,2],[2,4],[3,6]],[[1,2]]))
