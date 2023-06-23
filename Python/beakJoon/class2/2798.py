N, M = list(map(int,input().split()))

arr = list(map(int,input().split()))

Max = 0

for i in range(0,N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            target =(arr[i]+arr[j]+arr[k])
            if ((target) > M):
                continue
            elif(Max < target):
                Max = target
print(Max)