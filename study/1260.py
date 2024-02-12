from collections import deque

N , M , V = map(int,input().split())

graph = [ [] for i in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    a , b =map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in graph:
    i.sort()
def DFS(graph,start,visited):
    visited[start] = 1
    print(start,end=' ')

    for i in graph[start]:
        if (visited[i] != 1):
            DFS(graph,i,visited)

def BFS(graph,start,visited):
    queue = deque([start])
    visited[start] = 1
    while queue:
        v = queue.popleft()
        print(v , end= ' ')
        for i in graph[v]:
            if visited[i] != 1:
                visited[i] = 1
                queue.append(i)
    

DFS(graph,V,visited)
print()
visited =[0] *(N+1)
BFS(graph,V,visited)
print()

