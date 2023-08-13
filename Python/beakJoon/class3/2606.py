from collections import deque
N = int(input())
C = int(input())

graph = [[] for i in range(N+1)]
visited = [0]*(N+1)
for i in range(C):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited[1] = 1
count = 0
def DFS(x):
    global count
    visited[x] = 1
    count+=1
    for node in graph[x]:
        if visited[node]:
            continue
        else:
            DFS(node)
DFS(1)
print(count-1)