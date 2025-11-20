import math
import sys

input = sys.stdin.readline

n = int(input())


subtract = n * 0.15
rate = []

def self_made_round(para):
    target = para - int(para)
    return int(para) if target < 0.5 else int(para+1)

for i in range(n):
    rate.append(int(input()))
rate.sort()
subtract = self_made_round(subtract)

final_rate = rate[subtract:len(rate)-subtract]

if len(final_rate) > 0:
    length = len(final_rate)
else:
    length = 1

print(self_made_round(sum(final_rate)/length))