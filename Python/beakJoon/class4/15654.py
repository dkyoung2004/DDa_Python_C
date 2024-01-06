N , M = map(int,input().split())
arr = sorted(list(map(int,input().split())))
s = []
def DFS(start):
    if len(s) == M:
        print(' '.join(map(str,s)))
        return
    for i in range(start,N):
            s.append(arr[i])
            DFS(i)
            s.pop()
DFS(0)
