
while(1):
    N =int(input())
    cnt=[]
    if(N!=-1):
        for i in range(1,N):
            if(N % i == 0):
                cnt.append(i)
        if (sum(cnt) == N):
            print(N ,"=",1,end=" ")
            for i in range(1,len(cnt)):
                print("+",cnt[i],end=" ")
        else:
            print(N,"is NOT perfect.")
    else:
        break