from collections import deque

N , M = map(int,input().split())

world = []
visited = []
for _ in range(N):
    world.append(list(map(str,input())))
for _ in range(N):
    visited.append([0 for _ in range(M)])
print(visited)

dy = [0,0,-1,1]
dx = [-1,1,0,0]

def DFS(graph,a,b):
    cnt = 0
    queue = deque()
    queue.append((a,b))
    visited[a][b] = 1

    while queue:
        ay , ax = queue.popleft()
        for i in range(4):
            nx = ax+dx[i]
            ny = ay+dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if graph[ny][nx] == 0:
                continue
            if graph[ny][nx] ==1:
                graph[ny][nx] += (graph[a][b]+1)
                queue.append((ny,nx))
    return graph[N-1][M-1]

print(DFS(world,0,0))