def Factorial(N):
    if N <= 1:
        return 1
    else:
        return N*Factorial(N-1)

N = int(input())
print(Factorial(N))