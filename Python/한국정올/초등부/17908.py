import sys

input =  sys.stdin.readline

N = int(input())
arr = []
count = 0
for _ in range(N):
    arr.append(int(input()))
vision = 0
arr.reverse()
for i in range(N):
    if arr[i] > vision:
        count +=1
        vision = arr[i]
print(count)