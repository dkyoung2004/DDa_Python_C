import math

Case = int(input())

#순열의 개념을 활용해야함
for i in range(0,Case):
    arr = list(map(int,input().split()))
    N = arr[0]
    M = arr[1]
    print(int((math.factorial(M))/((math.factorial(N)*math.factorial(M-N)))))
