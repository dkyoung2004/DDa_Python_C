import sys
input = sys.stdin.readline

N , K = map(int,input().split())
dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1,N+1):
    Weight , Value = map(int,input().split())
    for j in range(1,K+1):
        if(j < Weight):
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-Weight]+Value)
print(max(dp[N]))