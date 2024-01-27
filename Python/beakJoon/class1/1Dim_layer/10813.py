N , M = map(int,input().split())
ball = [i for i in range(1,N+1)]

for _ in range(M):
    a , b = map(int,input().split())
    var_ = ball[b-1]
    ball[b-1] = ball[a-1]
    ball[a-1] = var_

for i in ball:
    print(i,end= ' ')