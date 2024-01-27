N = int(input())
A = list(map(int,input().split()))
max_1 = 0
minimum = A[0]
for i in A:
    if max_1 < i:
        max_1 = i
    elif minimum > i:
        minimum = i
print(minimum,max_1)
