steps=int(input())
count=0
while steps>0:
    if steps % 2 == 1:
        count+=1
        steps-=1
    elif steps % 2==0:
        steps-=(steps//2)
        count+=1
print(count)
        
