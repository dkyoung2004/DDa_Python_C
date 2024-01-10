import sys
input = sys.stdin.readline

n , m = map(int,input().split())

arr = sorted(list(map(int,input().split())))
graph = []
temp = []
def DFS(start):
    prev = 0
    if (len(graph) == m ):
        print(' '.join(map(str,graph)))
        return
    for i in range(start,n):
        if arr[i] != prev:
            prev = arr[i]
            graph.append(arr[i])
            DFS(i)
            graph.pop()

DFS(0)