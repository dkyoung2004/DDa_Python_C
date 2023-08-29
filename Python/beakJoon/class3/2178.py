N , M = map(int,input().split())

world = []
visited = []
for _ in range(N):
    world.append(list(map(str,input())))
for _ in range(N):
    visited.append([0 for _ in range(M)])
print(visited)

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def BFS():