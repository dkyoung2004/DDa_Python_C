from collections import deque
N,L,S = map(int, input().split())
graph = [[] for i in range(N+1)]
for i in range(L):
    a , b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0] * (N+1)
for i in range(len(graph)):
        graph[i] = sorted(graph[i])
def DFS(graph,v,visited):
    print(v, end = ' ')
    visited[v] = 1
    for node in graph[v]:
        if visited[node] != 1:
            DFS(graph,node,visited)
DFS(graph,S,visited)
visited = [0] * (N+1)
print('')
def BFS(graph,v,visited):
    queue = deque([v])
    visited[v] = 1
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if (visited[i]!=1):
                queue.append(i)
                visited[i] = 1
BFS(graph,S,visited)