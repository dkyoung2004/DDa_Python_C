def Fibonacci(N):
    if N <= 0 :
        return 0
    elif N == 1:
        return 1
    else:
        return Fibonacci(N-2)+Fibonacci(N-1)
    
N = int(input())
print(Fibonacci(N))