import sys

input = sys.stdin.readline


N = int(input())
total = 0
arr = []
cnt = 0
for i in range(N):
    a = int(input())
    total += a
    arr.append(a)

arr = sorted(arr)

dic = dict()
for i in arr:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

mx = max(dic.values())
mx_dic = []

for i in dic:
    if mx == dic[i]:
        mx_dic.append(i)

print(round(total/N))
print(arr[(N//2)])
if len(mx_dic) > 1:
    print(mx_dic[1])
else:
    print(mx_dic[0])
print(arr[N-1]-arr[0])
