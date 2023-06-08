import sys

input =  sys.stdin.readline

number = int(input())
#계수 정렬, 중복된 수가 많고 수의 범위가 한정되어있을때 사용
arr= [0] * 10001
# 최대 10000까지의 수를 넣는다고 했으니까 넉넉하게 10001개자리 확보
for i in range(0,number):
    arr[int(input())] += 1
for j in range(0,10001):
        if arr[j]!=0:
             for k in range(0,arr[j]):
                   print(j)