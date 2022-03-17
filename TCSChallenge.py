
class Blood:
    def __init__(self,bloodGroup,unitInHand):
        self.bloodGroup=bloodGroup
        self.unitInHand=unitInHand
class BloodBank:
    
    def __init__(self,bloodList):
        self.bloodList=bloodList
    def isBloodAvailable(self,blood,units):
        for i in range(len(self.bloodList)):
            if self.bloodList[i][0]==blood and self.bloodList[i][1]>=units:
                return True
        else:
            return False
    def findMinBloodStock():
        pass
n=int(input("Enter No of Blood Groups: "))
list1=[]
for i in range(n):
    blood=input("Enter blood group: ")
    units=int(input("Enter units available: "))
    list1.append([blood,units])
blood=input("Enter required blood group: ")
units=int(input("Enter required units: "))
B1=BloodBank(list1)
if B1.isBloodAvailable(blood,units)==True:
    print("Blood Available")
    print(blood)
else:
    print("Blood Not Available.")
