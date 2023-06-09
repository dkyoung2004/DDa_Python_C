import math

M ,N= map(int,input().split())
def Prime(n):
    if n == 1:
        False
    else:
        for i in range(2,int(math.sqrt(N))+1):
            if k%i==0:
                return False
        return True
        
for k in range(M,N+1):
    if Prime(k):
        print(k)
    

