import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
sort_set = list(set(arr))
sort_set = sorted(sort_set)
dic = {sort_set[i]: i for i in range(0,len(sort_set))}
for i in arr:
    print(dic[i],end=" ")

    