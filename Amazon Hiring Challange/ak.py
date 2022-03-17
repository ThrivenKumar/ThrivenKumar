def combine(parts):
    list1=[]
    list2=list(set(parts))
    for i in range(len(list2)-1):
        mini=list2[0]
        for j in list2:
            if mini>j:
                mini=j
        one=mini
        list2.remove(mini)
        mini=list2[0]
        for j in list2:
            if mini>j:
                mini=j
        two=mini
        list2.remove(mini)
        three=one+two
        list1.append(three)
        list2.append(three)
    count=0
    for i in list1:
        count+=i
    return count

print(combine([4,20,4,8,2]))
