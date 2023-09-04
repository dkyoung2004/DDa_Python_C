import heapq
import sys

input = sys.stdin.readline

heap = []
N = int(input())

for _ in range(N):
    M =  int(input())
    if M != 0:
        heapq.heappush(heap,(abs(M),M))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)
        

    