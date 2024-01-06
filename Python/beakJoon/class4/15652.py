N, M = map(int,input().split())

visited = [0] * (N+1)
arr = []

def DFS(start):
    if (len(arr) == M):
        print(' '.join(map(str,arr)))
        return
    for i in range(start,N+1):
            arr.append(i)
            DFS(i)
            arr.pop()
DFS(1)