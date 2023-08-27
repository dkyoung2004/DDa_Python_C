import heapq
import sys

input = sys.stdin.readline
heap = []
I = int(input())
for i in range(I):
    a = int(input())
    a = (a*-1)
    if (a == 0):
        if(len(heap) == 0):
            print(0)
        else:
            print(-1*(heapq.heappop(heap)))
    else:
        heapq.heappush(heap,a)
