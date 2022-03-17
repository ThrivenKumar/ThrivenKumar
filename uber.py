n=int(input())
list1=input().split(" ")
list2=input().split(" ")
mini1=int(list1[0])
index1=0
mini2=int(list2[0])
index2=0
for i in range(n):
    if int(list1[i])<mini1:
        mini1=int(list1[i])
        index1=i
    if int(list2[i])<mini2:
        mini2=int(list2[i])
        index2=i
total_count=0
if mini2>mini1:
    for i in range(n):
        if i==index1:
            continue
        else:
            total_count+=int(list2[i])*mini1
else:
      for i in range(n):
        if i==index2:
            continue
        else:
            total_count+=int(list1[i])*mini2
print(total_count)
    
