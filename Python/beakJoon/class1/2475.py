arr = list(map(int,input().split()))

arr = list(map(lambda x : x**2, arr))
total  = 0
for i in arr:
    total+=i

print(total%10)