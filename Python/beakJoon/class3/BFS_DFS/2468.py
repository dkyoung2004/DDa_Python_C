from collections import deque

N = int(input())
graph = []

for _ in range(N):
    graph.append(list(map(int,input().split())))

def BFS():
    q = deque()
    while q:
        a = q.popleft()
for i in range(max(graph)):
