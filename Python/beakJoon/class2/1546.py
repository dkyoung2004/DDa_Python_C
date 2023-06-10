N = int(input())

arr=list(map(int,input().split()))
arr.sort(reverse=True)
total = 0
for i in range(0,N):
    total+=((arr[i]/arr[0])*100)
print(total/N )
