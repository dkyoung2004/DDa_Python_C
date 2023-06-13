from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
interpret = []
a = deque()
for i in range(0,N):
    interpret= input().split()
    if(interpret[0] == "push_front"):
        a.appendleft(interpret[1])
    elif(interpret[0] == "push_back"):
        a.append(interpret[1])
    elif(interpret[0] == "pop_front"):
        if (len(a)==0):
            print(-1)
        else:
            print(a.popleft())
    elif(interpret[0] == "pop_back"):
        if (len(a)==0):
            print(-1)
        else:
            print(a.pop())
    elif(interpret[0] == "size"):
        print(len(a))
    elif(interpret[0] == "empty"):
        if (len(a)==0):
            print(1)
        else:
            print(0)
    elif(interpret[0] == "front"):
        if (len(a)==0):
            print(-1)
        else:
            print(a[0])
    elif(interpret[0] == "back"):
        if (len(a)==0):
            print(-1)
        else:
            print(a[(len(a)-1)])
    