N, M = map(int,input().split())

BFS_arr =[]
visited =[0]
s = []

for i in range(1,N+1):
    BFS_arr.append(i)
    visited.append(0)
def DFS():
    if len(s)==M:
        print(' '.join(map(str,s)))
        return
    for i in range(1,N+1):
        if visited[i]==1:
            continue
        visited[i] = 1
        s.append(i)
        DFS()
        s.pop()
        visited[i] = 0
DFS()