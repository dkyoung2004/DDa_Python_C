n = int(input())
graph = list(map(int,input().split()))
DP = [0] * n
DP[0] = graph[0]
for i in range(1,n):
    DP[i] = max(DP[i-1]+graph[i] , graph[i])
print(max(DP))