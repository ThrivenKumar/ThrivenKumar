input1=int(input())
num=''
while input1>0:
    num =num+str( input1%2)
    input1=input1//2
num2=num[::-1]
setbits=0
msb=0
lsb=0
length=len(num2)
for i in range(length):
    if num2[i]=='1':
        setbits=setbits+1
        lsb=i
for i in range(length):
    if num2[i]=='1':
        msb=i
        break
print(setbits,'#',length-lsb-1,'#',length-msb-1)
    
    
