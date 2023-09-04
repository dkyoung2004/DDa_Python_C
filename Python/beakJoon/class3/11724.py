import sys

sys.setrecursionlimit(5000)
input = sys.stdin.readline


def DFS(x):
    visited[x] = 1
    for i in node[x]:
        if visited[i] == 0:
            DFS(i)


N , M = map(int,input().split())
node = [[] for _ in range(N+1)]
visited =[0 for _ in range(N+1)]
cnt = 0

for _ in range(M):
    a , b = map(int,input().split())
    node[a].append(b)
    node[b].append(a)
for i in range(1,N+1):
    if visited[i] == 0:
        DFS(i)
        cnt+=1
    else:
        continue
print(cnt)
    
    

