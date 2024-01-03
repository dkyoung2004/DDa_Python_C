n = int(input())
dp = [0 for i in range(n)]
box = list(map(int,input().split()))
dp[n-1] = 1
temp = [0]
for i in range(n-2,-1,-1):
    for j in range(i,n):
        if box[i] < box[j]:
            temp.append(dp[j])
    dp[i]= max(temp)+1
    temp = [0]
print(max(dp))