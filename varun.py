size=int(input())
numbers=[]
def func(size):
    for i in range(size):
        temp=int(input())
        if temp not in numbers:
            numbers.append(temp)
        else:
            print("INVALID INPUT")
            return
    n=int(input())
    half=size//2
    if n>=half:
        for i in range((size-n)+1):
            max=numbers[0]
            for j in range(size):
                if numbers[j]>max:
                    max=numbers[j]
            numbers.remove(max)
            size=size-1
            n=n-1
        print(max)
    else:
        for i in range(n):
            min=numbers[0]
            for j in range(size):
                if numbers[j]<min:
                    min=numbers[j]
            numbers.remove(min)
            size=size-1
            n=n-1
        print(min)
func(size)
