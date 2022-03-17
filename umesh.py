list1=input().split()
list2=input().split()
list3=input().split()
n=int(list1[0])
x=int(list1[1])
k=int(list1[2])
for i in range(n):
    list2[i]=int(list2[i])
booli=True
days = 0
while booli:
    count=0
    for i in list2:
        if int(i)>k:
            count+=int(i)
    if count>=x:
        break
    days+=1
    for i in range(n):
        list2[i]+=int(list3[i])
print(days)
        
            

