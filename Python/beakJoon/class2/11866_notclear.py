N , K = map(int,input().split())
arr = []
index = 0
print("<",end="")
for i in range(1,N+1):
    arr.append(i)
while len(arr) > 1:
    index = 1
    print(arr[index],end =", ")
    del arr[index]
print(arr[0],end="")
print(">")