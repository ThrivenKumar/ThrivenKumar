import math
def func(n):
    if n<0:
        print("Wrong Input")
        return 

    n1=n
    temp=0
    while n>0:
        temp+=1
        n=n//10

    tens=int(math.pow(10,temp))
    power=math.pow(n1,4)
    power=power-n1
    if power%tens==0:
        print("True")
    else:
        print("False")

n=int(input())
func(n)
