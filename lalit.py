def validQuadriples(N,A):
     s1=0
    s2=0
    serv=0
    for i in range(N):
        if s1>=s2:
            serv=0
            if S[i]=="W":
                s1+=1
            else:
                s2+=1
        else:
            serv=1
            if S[i]=="W":
                s2+=1
            else:
                s1+=1
        print(s1,s2)

        
