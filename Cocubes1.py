def SumofGCD(k,arr,n):
    def gcd(a, b): 
        if a == 0 :
            return b 
        return gcd(b%a, a)
    sum=0
    if n<=0:
        return -1
    else:
        for i in arr:
            sum+=gcd(k,i)
    return sum
print(SumofGCD(4,[3,8,1,10,6,3,1],7))
