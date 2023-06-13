N , K = map(int,input().split())
maxnum=0
for i in range(1,N+1):
    if(((N%i==0)and (K%i==0))):
        num = i
        if(num>maxnum):
            maxnum = num

print(maxnum)
print(int((N*K)/maxnum))