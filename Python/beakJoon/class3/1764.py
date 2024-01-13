n,m = map(int,input().split())
count=0
arr = set()
arr_out = set()


for i in range(n):
    arr.add(input())
for j in range(m):
    arr_out.add(input())

result = sorted(list(arr & arr_out))

print(len(result))
for value in result:
    print(value)