n=int(input())
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact
i=2
total=0
while i<n:
    denom=factorial(i)*factorial(n-i)
    numer=factorial(n)
    total+=int((numer/denom)+n)
    i=i+2
print(total)
