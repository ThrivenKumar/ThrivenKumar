t=int(input())

def isPossible(n,k,s):
    lis1=[]
    booli=True
    for i in range(n):
        lis1.append(s[i])
        if s[i]=='1':
            booli=False
    if booli==True:
        print(1)
    else:
        z=0
        booli=True
        for i in range((n-k+1)):
            if lis1[i]=='1':
                z=i
                for j in range(k):
                    if lis1[z+j]=='0':
                        lis1[z+j]='1'
                    else:
                        lis1[z+j]='0'
                i=0
        for i in range(n):
            if lis1[i]=='1':
                booli=False
        if booli==True:
            print(1)
        else:
            print(0)
            
        
for i in range(t):
    n=int(input())
    k=int(input())
    s=input()
    isPossible(n,k,s)
