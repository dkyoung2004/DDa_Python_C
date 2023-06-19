a,b,c = list(map(int,input().split()))
total = (a+b+c)
arr = [0] * (total)
comparison = 0
for i in range(1,a+1):
    for j in range(1,b+1):
        for k in range(1,c+1):
            arr[i+j+k-1] +=1
    

print(arr.index(max(arr))+1)
