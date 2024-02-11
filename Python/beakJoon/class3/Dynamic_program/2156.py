import sys

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

DP = [0] * (n+3)
DP[0] = arr[0]

if n > 1:
    DP[1] = arr[0]+arr[1]
if n > 2:
    DP[2] = max(arr[0]+arr[2] , arr[1]+arr[2],DP[1])
for i in range(3,n):
    DP[i] = max(DP[i-2]+arr[i] , DP[i-3] + arr[i-1]+arr[i] , DP[i-1])

print(DP[n-1])