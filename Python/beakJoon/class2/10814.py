N = int(input())
arr=[]
for i in range(0,N):
    arr.append(input().split())
    arr = map(int,arr[i][0])
a = sorted(arr,key = lambda x:x[0])

for i in a:
    print(i[0],i[1])