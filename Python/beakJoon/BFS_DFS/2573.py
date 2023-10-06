from collections import deque

N, M = map(int,input().split())

glacier = []
first_location = []
visit = []
for i in range(N):
    glacier.append(list(map(int,input().split())))
    visit.append([0 for _ in range(M)])
print(visit)

#N이 y값
#M이 x값

dx = [0,0,-1,1]
dy = [-1,1,0,0]

for i in range(N):
    for j in range(M):
        if(glacier[i][j] != 0):
            first_location = [i,j]
            break
    if(first_location != []):
        break
def BFS():
    q = deque()
    q.append(first_location)
    roop = 1
    while q:
        y,x = q.popleft()
        ocean_count = 0
        visit[y][x] +=1
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            if (ax > 0 and ax <= M) and (ay > 0 and ay <= N):
                if(glacier[ay][ax] <= 0):
                    ocean_count = 1
                if(glacier[ay][ax] >= 1):
                    if(visit[ay][ax])):
                    else:
                        q.append([ay,ax])
        if(ocean_count == 1):
            glacier[y][x] -= 1
        for i in range(N):
            for j in range(M):
                print(visit[i][j],end=' ')
            print('')
    print(0)
BFS()