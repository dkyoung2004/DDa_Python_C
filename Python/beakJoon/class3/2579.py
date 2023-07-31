N = int(input())
stair =[]
dp = [0]*N
for i in range(N):
    stair.append(int(input()))
if len(stair)<=2:
    print(sum(stair))
else:
    dp[0] = stair[0]
    dp[1] = stair[1] + stair[0]
    for i in range(2,N):
        dp[i] = max(dp[i-3]+stair[i-1]+stair[i],dp[i-2]+stair[i])
    print(dp[-1])