import sys

input = sys.stdin.readline


N , M = map(int,input().split())
arr = list(map(int,input().split()))


def Prefix_Sum():
    for i in range(1,N):
        arr[i] = arr[i-1] + arr[i]

Prefix_Sum()
arr.insert(0,0)
for i in range(M):
    start , end = map(int,input().split())
    print(arr[end]-arr[start-1])