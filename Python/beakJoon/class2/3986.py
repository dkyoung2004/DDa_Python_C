import sys

input = sys.stdin.readline
N = int(input())
count = 0
for _ in range(N):
    arr = input().rstrip()
    stack = []
    for i in range(len(arr)):
        if stack and arr[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(arr[i])
    if not stack:
        count +=1
print(count)