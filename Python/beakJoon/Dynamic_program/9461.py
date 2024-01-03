Test_case = int(input())
dp = [1,1,1]
for i in range(3,100):
    dp.append(dp[i-3]+dp[i-2])
for i in range(Test_case):
    k=int(input())
    print(dp[k-1])