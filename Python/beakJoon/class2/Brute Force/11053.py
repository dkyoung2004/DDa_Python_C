N = int(input())
A = list(map(int,input().split()))
B = [1] * (N)

for i in range(N-2,-1,-1):
    for j in range(i,N):
        if A[i]<A[j]:
            B[i] = max(B[i],B[j]+1)
print(max(B))
