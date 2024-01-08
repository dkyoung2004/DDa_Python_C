N , K = map(int,input().split())
cnt = []
for i in range(1,N+1):
    if(N % i == 0):
        cnt.append(i)
if(K > len(cnt)):
    print(0)
else:
    print(cnt[K-1])