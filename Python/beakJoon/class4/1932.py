floor = int(input())
dp = []
for _ in range(0,floor):
    dp.append(list(map(int,input().split())))

for i in range(1,floor):
    for j in range(i+1):
        if j==0:
            dp[i][j]+=dp[i-1][j]
        elif j==i:
            dp[i][j]+=dp[i-1][j-1]
        else:
            dp[i][j] += max(dp[i - 1][j - 1], dp[i - 1][j])
print(max(dp[floor-1]))