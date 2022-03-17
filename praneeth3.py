import math
def calRunDistance(length,diagonal,rounds):
    breadth=math.sqrt((diagonal*diagonal)-(length*length))
    round1=2*(length+breadth)
    totaldistance=round1*rounds
    return totaldistance
if __name__=='__main__':
    n=int(input())
    m=int(input())
    rounds=int(input())
    if rounds>0:
        print(int(calRunDistance(n,m,rounds)))
    else:
        print("Invalid input")
