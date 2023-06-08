X = 0
N = 0
a = b = 0

X = int(input())
N = int(input())
price = 0
for i in range(0,N):
    a,b = map(int,input().split())
    X -= (a * b)
if X != 0:
    print("No")
else:
    print("Yes")