import sys

input = sys.stdin.readline


N = int(input())

arr = set()
count = 0
for _ in range(N):
    scheme = input()
    if(scheme == "ENTER\n"):
        arr.clear()
    elif(scheme not in arr):
        arr.add(scheme)
        count+=1
print(arr)
print(count)