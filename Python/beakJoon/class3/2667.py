from collections import deque

N , M = map(int,input().split())

world = []
for _ in range(N):
    world.append(list(map(int,input())))

dy = [0,0,-1,1]
dx = [-1,1,0,0]

def DFS(graph,a,b):
    queue = deque()
    queue.append((a,b))

    while queue:
        ax , ay = queue.popleft()
        for i in range(4):
            nx = ax+dx[i]
            ny = ay+dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
print(DFS(world,0,0))