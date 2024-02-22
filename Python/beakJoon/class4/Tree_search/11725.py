from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
node = [[] for i in range(N+1)]

for i in range(N-1):
    A , B = map(int,input().split())
    node[A].append(B)
    node[B].append(A)

parents = [0] * (N+1)
visited = [0] * (N+1)
def DFS():
    q = deque()
    q.append(1)
    while q:
        a = q.popleft()
        if (visited[a] != 1):
            visited[a] = 1
            for i in node[a]:
                if(visited[i] != 1):
                    parents[i] = a
                    q.append(i)
DFS()
for i in range(2,N+1):
    print(parents[i])