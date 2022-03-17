import itertools
n=int(input())
given = input()
list1=[]
for i in range(n):
    
    list1.append(given[i])
def findsubsets(s,n):
    for i in range(1,n+1):
        for i in list(itertools.combinations(s,i)):
            string=""
            for j in range(len(i)):
                string+=i[j]
            print(string)
                
  
  
findsubsets(list1,n)
