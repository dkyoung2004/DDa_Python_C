import sys

input = sys.stdin.readline

M = int(input())
N = set()
for i in range(0,M):
    query = list(input().split())
    if(query[0] == "add"):
        query[1] = int(query[1])
        N.add(query[1])
    elif(query[0] == "remove"):
        query[1] = int(query[1])
        N.discard(query[1])
    elif(query[0] == "check"):
        query[1] = int(query[1])
        if(query[1] in N):
            print(1)
        else:
            print(0)
    elif(query[0] == "toggle"):
        query[1] = int(query[1])
        if(query[1] in N):
            N.remove(query[1])
        else:
            N.add(query[1])
    elif(query[0] == "all"):
        N = set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    elif(query[0] == "empty"):
        N = set()
