N = int(input())

def isPrime(Num):
    if(Num == 1):
        return False
    else:
        for i in range(2,int(Num**0.5)+1):
            if (Num % i)==0:
                return False
        return True
        
Count = 0
M = list(map(int,input().split()))
for j in M:
    if isPrime(j):
        Count+=1
print(Count)
    
