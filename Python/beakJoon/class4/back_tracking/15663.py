import sys
input = sys.stdin.readline

n , m = map(int,input().split())

arr = sorted(list(map(int,input().split())))
graph = []
temp = []
visited = [0 for _ in range(n)]
def DFS():
    prev = 0
    if (len(graph) == m ):
        print(' '.join(map(str,graph)))
        return
    for i in range(n):
        if arr[i] != prev and visited[i] == 0 :
            graph.append(arr[i])
            prev = arr[i]
            visited[i] = 1
            DFS()
            graph.pop()
            visited[i] = 0

DFS()