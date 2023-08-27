from collections import deque
M , N , H = map(int,input().split())

box = [[] for _ in range(H)]
visited = [[] for _ in range(H)]
for i in range(H):
    for _ in range(N):
        box[i].append(list(map(int,input().split())))
for i in range(H):
    for _ in range(N):
        visited[i].append(list(0 for i in range(len(box[0][0]))))
location_set = []
dx = [0,0,0,0,-1,1]
dy = [0,0,-1,1,0,0]
dz = [-1,1,0,0,0,0]

#최초의 익은 토마토 좌표 찾기 
for i in range(H):
    for j in range(N):
        for k in range(M):
            if(box[i][j][k] == 1):
                location_set.append([k,j,i])                
def BFS(box,visited,location_set):
    set1 = deque(location_set)
    set2 = []
    roop = 0
    
    while set1:
        x,y,z = set1.popleft()
        visited[z][y][x] = 1
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx < 0 or nx >= M or ny < 0 or  ny >= N or nz < 0 or nz >= H:
                continue
            if (visited[nz][ny][nx] == 0 and box[nz][ny][nx] == 0):
                visited[nz][ny][nx] = 1
                box[nz][ny][nx] = 1
                set2.append([nx,ny,nz])
        if (len(set1) == 0):
            roop +=1
            set1 = deque(set2)
            set2.clear()
    roop -= 1
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if(box[i][j][k] == 0):   
                    roop = -1



    return roop
    



    

print(BFS(box,visited,location_set))

