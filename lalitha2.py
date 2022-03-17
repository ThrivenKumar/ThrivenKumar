class UserMainCode:
    def isPalindrome(self,inputstring):
        j=len(inputstring)-1
        rangeval=(len(inputstring)//2)
        for i in range(rangeval):
            if inputstring[i]!=inputstring[j]:
                return 0
            j-=1
        return 1
    def countPalindromes(self,input1,input2):
        input1=input1.split(" ")
        count=0
        for i in range(len(input1)):
            if input1[i].isalpha():
                 flag=self.isPalindrome(input1[i])
                 if flag==1:
                     count+=1
        return count
    
obj=UserMainCode()
input1=input()
input2=input()
print(obj.countPalindromes(input1,input2))

