N = int(input())

def DP(a):
    if a == 1:
        return 1
    if a == 2:
        return 2
    if a == 3:
        return 4
    else:
        return DP(a-1)+DP(a-2)+DP(a-3)

for _ in range(N):
    a = int(input())
    print(DP(a))
