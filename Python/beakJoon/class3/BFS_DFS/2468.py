from collections import deque

N = int(input())
graph = []
wait = []
for _ in range(N):
    graph.append(list(map(int,input().split())))

def BFS(table):
    q = deque()
    q.append(table)
    while q:
        y , x = q.popleft()
        dx = [-1,1,0,0]
        dy =[0,0,-1,1]
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            if(0 <= ax < N and 0 <= ay < N and graph[ay][ax] != 0):
                q.append([ay,ax])
                



for i in range(max(graph)):
    for j in range(N):
        for k in range(N):
            if (graph[j][k] <= i):
                graph[j][k] = 0
            else:
                wait.append([j,k])
    BFS(wait)
    