A, B, C = map(int,input().split())

def DAF(a,b,c):
    if(b == 1):
        return a%c
    elif(b % 2 == 0):
        return(DAF(a,b//2,c)**2)%c
    else:
        return((DAF(a,b//2,c)**2)*a)%c
print(DAF(A,B,C))
