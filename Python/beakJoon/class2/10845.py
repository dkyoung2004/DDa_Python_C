import sys
from collections import deque
input = sys.stdin.readline

order = []
arr = deque()
for i in range(int(input())):
    order = list(map(str,input().split()))
    if(order[0] == "push"):
        arr.append(order[1])
    elif(order[0] == "pop"):
        if(len(arr)!=0):
            print(arr.popleft())
        else:
            print(-1)
    elif(order[0] == "size"):
        print(len(arr))
    elif(order[0] == "empty"):
        if((len(arr))!=0):
            print(0)
        else:
            print(1)
    elif(order[0] == "front"):
        if((len(arr))!=0):
            print(arr[0])
        else:
            print(-1)
    elif(order[0] == "back"):
        if((len(arr))!=0):
            print(arr[len(arr)-1])
        else:
            print(-1)