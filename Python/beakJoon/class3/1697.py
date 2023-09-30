from collections import deque


a, b = map(int,input().split())

short_way = 0
def bfs():
   q = deque()
   q.append(a)
   while q:
      x = q.popleft()
      

print(bfs(a,0))