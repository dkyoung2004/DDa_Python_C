
N = int(input())
K = list(map(int,input().split()))

total = 0
miss = 0

for i in K:
    total += i
total_visited = [0] * (total+1)

def DFS(limit,value):
    if limit == N:
        if( 0 < value and value <= total):
            total_visited[value] = 1
    else:
        DFS(limit+1,(value-K[limit]))
        DFS(limit+1,value+K[limit])
        DFS(limit+1,value)
DFS(0,0)
print(total_visited.count(0)-1)