import sys

input = sys.stdin.readline

N = int(input())
a = 100
b=100

for _ in range(N):
    a_value , b_value = map(int,input().split())
    if (a_value < b_value):
        a -= b_value
    elif(a_value == b_value):
        continue
    else:
        b -= a_value

print(a)
print(b)