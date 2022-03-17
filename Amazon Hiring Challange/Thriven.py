def func(orderList):
    nonprime=[]
    prime=[]
    for i in orderList:
        temp=i.split(" ")
        if temp[1].isdigit():
            nonprime.append(i)
        else:
            prime.append(i)
    dictionary={}
    temp=[]
    list1=[]
    for i in prime:
        temp=i.split(" ",1)
        list1.append(temp)
    for i in range(len(prime)):
        mini=i
        count=0
        for j in range(i+1,len(prime)):
            if list1[i][1]==list1[j][1]:
                if list1[i][0]>list1[j][0]:
                    mini=j
                    count=1
                else:
                    mini=i
                    count=1
            elif list1[i][1]>list1[j][1]:
                mini=j
                count=1
        if count==1:
            temp=list1[i]
            list1[i]=list1[j]
            list1[j]=temp
    prime.clear()
    for i in range(len(list1)):
        prime.append(list1[i][0]+" "+list1[i][1])
    prime.extend(nonprime)
    return prime
print(func(["zld 93 12","fp kindle book","10a echo show","17g 12 25 6","ab1 kindle","125 echo dot second generation"]))
