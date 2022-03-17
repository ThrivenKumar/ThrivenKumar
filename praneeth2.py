def findValue(a,b):
    c=len(a)
    d=len(b)
    if c<d:
        return 0
    else:
        i=d-1
        while i>=0:
            c-=1
            if b[i]!=a[c]:
                return 0
            i-=1
        return 1
string1=input()
string2=input()
returnvalue=findValue(string1,string2)
if returnvalue==1:
    print("Yes")
elif returnvalue==0:
        print("No")
else:
    print("no")
    
