import math
 
def Nth_of_GP(a, r, N):
    return( a * (int)(math.pow(r, N - 1)) )

second=int(input())
third=int(input())
n=int(input())
r=third/second
a=second/r

print(format(Nth_of_GP(a, r, n),".3f"))
