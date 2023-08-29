N = int(input())

arr = []
arr = (list(map(int,input().split())))
arr.sort()
var = 0
total = 0
for i in range(N):
    var += arr[i]
    total += var
print(total)