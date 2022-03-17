def maximum_length (N, S, Q, X, Y):
    nstr=[]
    for i in range(N):
        nstr.append(S[i])
    ans=[]
    for i in range(Q):
        print(X[i]-1)
        nstr[X[i]-1]=Y[i]
        temp=substring(nstr,N)
        ans.append(temp)
    return ans

def substring(s,n):
    ans,temp=1,1
    for i in range(1,n):
        if s[i]==s[i-1]:
            temp+=1
        else:
            ans=max(temp,ans)
            temp=1
    ans=max(temp,ans)
    return ans

T = int(input())
for _ in range(T):
    N = int(input())
    S = input()
    Q = int(input())
    X = list(map(int, input().split()))
    Y = input().split()

    out_ = maximum_length(N, S, Q, X, Y)
    print (' '.join(map(str, out_)))

