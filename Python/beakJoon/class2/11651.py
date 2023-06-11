N = int(input())
arr=[]
for i in range(0,N):
    x, y = map(int,input().split())
    arr.append((x,y))

a = sorted(arr,key = lambda x:(x[1],x[0]))
for i in range(0,N):
    print(a[i][0],a[i][1])
