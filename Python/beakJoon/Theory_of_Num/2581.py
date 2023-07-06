N = int(input())
M = int(input())

def isPrime(Num):
    if(Num == 1):
        return False
    else:
        for i in range(2,int(Num**0.5)+1):
            if (Num % i)==0:
                return False
        return True
        
Count = []
Sum = 0
for i in range(N,M+1):
    if isPrime(i):
        Sum += i
        Count.append(i)
if(len(Count)!=0):
    print(Sum)
    print(Count[0])
else:
    print(-1)
    