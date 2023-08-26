from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

y ,x  = map(int, input().split())
graph = []
for i in range(y):
    graph.append(list(map(str,input())))
visited = [[0]*x for _ in range(y)]
I_location = [[i,j] for i in range(y) for j in range(x) if graph[i][j] == 'I']
def DFS(graph,a,b,visited):
    cnt = 0
    queue = deque()
    queue.append((a,b))
    visited[a][b] = 1

    while queue:
        ay , ax = queue.popleft()
        for i in range(4):
            nx = ax+dx[i]
            ny = ay+dy[i]
            if nx < 0 or nx >= x or ny < 0 or ny >= y:
                continue
            if graph[ny][nx] != 'X' and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                if graph[ny][nx] == 'P':
                    cnt+=1
                queue.append((ny,nx))
    return cnt
total = DFS(graph,I_location[0][0],I_location[0][1],visited) 
if total != 0 :
    print(total)
else:
    print('TT')
    
