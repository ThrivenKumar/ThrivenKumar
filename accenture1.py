from itertools import combinations
list1=input().split()
list2=[]
for i in list1:
    list2.append(int(i))
count=sum(list2)//2
maxi=0
count1=0
for i in range(len(list2)):
    data=combinations(list2,i+1)
    for j in list(data):
        if sum(j)>maxi:
            maxi=sum(j)
            count1=1
        elif sum(j)==maxi:
            count1=count1 + 1
if count1>1:
    print(maxi)

