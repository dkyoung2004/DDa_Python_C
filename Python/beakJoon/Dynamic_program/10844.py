N = int(input())

dp = [[0] * 10  for _ in range(N+1)]
for i in range(1,10):
    dp[0][i] = 1
for i in range(1,N):
    for j in range(0,10):
        if(j==0):
            dp[i][j+1] += dp[i-1][j]
        elif(j==9):
            dp[i][j-1] += dp[i-1][j]
        else:
            dp[i][j-1] += dp[i-1][j]
            dp[i][j+1] += dp[i-1][j]

print(sum(dp[N-1]))