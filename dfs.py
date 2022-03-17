from collections import deque
def dfs(graph,start,visited=None):
    if visited==None:
        visited=set()
    visited.add(start)
    print(" ",start," ")
    for i in graph[start]-visited:
        dfs(graph,i,visited)
graph={'0':set(['1','2']),
       '1':set(['0','3','4','5']),
       '2':set(['0','6']),
       '3':set(['1']),
       '4':set(['1']),
       '5':set(['1']),
       '6':set(['2'])
       }

def bfs(graph,start,visited=None):
    if visited==None:
        visited=set()
        queue=deque([start])
    visited.add(start)
    while queue:
        vertex=queue.popleft()
        print(vertex," ")
        for i in graph[vertex]:
            if i not in visited:
                visited.add(i)
                queue.append(i)
def toh(n,f,t,a):
    if n==1:
        print("move disk from",f,"to",t)
    else:
        toh(n-1,f,a,t)
        print("move disk from",f,"to",t)
        toh(n-1,a,t,f)
        return
toh(4,'a','c','b')


