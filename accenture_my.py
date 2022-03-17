from itertools import combinations
m=int(input())
n=int(input())
list1=[]
for i in range(m):
    list1.append(i+1)
combos=list(combinations(list1,4))
count=0
booli2=False
for i in range(len(combos)):
    booli2=True
    for j in range(n-1):
        if combos[i][j+1]<(2*combos[i][j]):
            booli2=False
    if booli2==True:
        count=count + 1
print(count)
