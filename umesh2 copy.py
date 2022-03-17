n=int(input())
list1=[]
for i in range(n):
    list1.append(input())
for i in range(n):
    newstring=list1[i][0]
    k=0
    for j in range(1,len(list1[i])):
        if list1[i][j] != newstring[k]:
            newstring+=list1[i][j]
            k=k+1
    print(newstring)
