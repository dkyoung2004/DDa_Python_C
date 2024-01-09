from collections import deque


n ,m =map(int,input().split())
arr = []
graph = []
locate_2=[]
visited =[]

def find(arr):
    for i in range(n):
        for j in range(m):  
            if(arr[i][j] == 2):
                return [i,j]

for _ in range(n):
    arr.append(list(map(int,input().split())))
    visited.append([0 for _ in range(m)])
    graph.append([0 for _ in range(m)])

locate_2 = find(arr)

def BFS():
    q = deque()
    q.append(locate_2)
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    while(q):
        y,x = q.popleft()
        for i in range(4):
            ax = x+ dx[i]
            ay = y+ dy[i]
            if ( (ax >= 0 and ay >= 0 ) and (ax < m and ay < n)):
                if(arr[ay][ax] == 1):
                    if(visited[ay][ax] == 0):
                        visited[ay][ax] = 1
                        graph[ay][ax] = graph[y][x] + 1
                        q.append((ay,ax))
    for i in range(n):
        for j in range(m):
            if(arr[i][j] == 1 and visited[i][j] == 0):
                graph[i][j] = -1
BFS()
for i in range(n):
    for j in range(m):
        print(graph[i][j],end= ' ')
    print()
            
