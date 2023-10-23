import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p = list(map(str,input()))
    n = int(input())

    loop = 0
    arr = input().rstrip()[1:-1].split(",")
    array = deque(arr)
    error = 0

    if n == 0:
        array = deque([])

    for i in p:
        if(i == 'R'):
            loop+=1
        elif(i == "D"):
            if len(array) < 1:
                print("error")
                error = 1
                break
            else:
                if loop % 2 == 0:
                    array.popleft()
                else:
                    array.pop()
    if(loop % 2 == 1):
        array.reverse()
    if(error == 0):
        print("[" + ",".join(array)+"]")
