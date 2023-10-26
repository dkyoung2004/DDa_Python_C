from collections import deque
import sys


input = sys.stdin.readline

N , M = map(int,input().split())

chest = []
tomato = []

for _ in range(M):
    chest.append(list(map(int,input().split())))
for i in range(M):
    for j in range(N):
        if(chest[i][j] == 1):
            tomato.append([i,j])

print(tomato)
def DFS():
    queue = deque(tomato)
    while queue:
        y,x = queue.popleft()
        dx = [0,0,-1,1]
        dy = [-1,1,0,0]
        for i in range(4):
            ax = dx[i]+x
            ay = dy[i]+y
            if ((0 <= ax and ax <= N-1) and (0<=ay and ay <=M-1)):
                if(chest[ay][ax] == 0):
                    chest[ay][ax] = 1
                    queue.append([ay,ax])
        
for i in range(M):
    for j in range(N):
        if(chest[i][j] == 1):
            print(-1)
DFS()
for i in range(M):
    print(chest[i],end ="\n")
    
        