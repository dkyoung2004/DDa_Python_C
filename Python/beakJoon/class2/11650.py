import sys

input = sys.stdin.readline
text = []
n = int(input())
b= []
for i in range(0,n):
    text.append(list(map(int,input().split())))
b = sorted(text)
for j in range(0,n):
    print(b[j][0] , b[j][1])

#마지막으로 출력만 다듬으면 완성
