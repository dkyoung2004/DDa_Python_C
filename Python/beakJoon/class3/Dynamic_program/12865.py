N , K = map(int,input().split())
arr = []
for i in range(N):
    arr.append(list(map(int,input().split())))

arr.sort()
DP = [0] * N
weight_DP = [0] * N
DP[0] = arr[0][1]
weight_DP = arr[0][0]

for i in range(N):
    