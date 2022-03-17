class UserMainCode(object):
    @classmethod
    def calcTotalTax(cls,input1,input2):
        
        count=0
        for i in range(input1):
            input2[i]=input2[i]-1000
        for i in range(input1):
            if input2[i]>=1000:
                count=count+(input2[i]//10)
        return count
        
