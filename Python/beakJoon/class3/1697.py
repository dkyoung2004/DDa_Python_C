from collections import deque


n, k = map(int,input().split())
Max = 100000
dist = [0]* (Max+1)
short_way = 0
def bfs():
   q = deque()
   q.append(n)
   t=0
   while q:
      x = q.popleft()
      if x == k:
         print(dist[x])
         break
      for nx in (x-1,x+1,2*x):
         if (0 <= nx) and (nx<= Max) and not dist[nx]:
            dist[nx] = 1 + dist[x]
            q.append(nx)
bfs()