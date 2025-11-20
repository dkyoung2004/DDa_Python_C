N = int(input())
arr = []
find = True
for i in range(N):
    arr = [int(d) for d in str(i)]
    arr.append(i)
    if sum(arr) == N:
        print(i)
        find = False
        break
if find :
    print(0)
