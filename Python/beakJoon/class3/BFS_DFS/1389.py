from collections import deque

N , M = map(int,input().split())
graph = []
for i in range(M):
    graph.append(list(map(int,input().split())))

visited = [0] * N
def BFS():
    q = deque(graph)
    while(q):
        for i in range(N):
