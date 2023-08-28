import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
time_table = []

for _ in range(N):
    a=(list(map(int,input().split())))
    time_table.append(a)
time_table.sort(key=lambda x:(x[1],x[0]))
time_table = deque(time_table)
time = 0
count = 0
for time_table in time_table:
    if time <= time_table[0]:
        time = time_table[1]
        count+=1

        
print(count)