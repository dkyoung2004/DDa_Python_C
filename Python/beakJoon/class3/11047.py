import sys

input = sys.stdin.readline

N , K = map(int,input().split())
wallet = []
for i in range(N):
    wallet.append(int(input()))
def GreedyAl(wallet,K):
    change = 0 
    for i in reversed(wallet):
        if i<=K:
            change += K // i
            K = K % i
    return change
print(GreedyAl(wallet,K))
