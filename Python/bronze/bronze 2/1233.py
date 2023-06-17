a,b,c = list(map(int,input().split()))
total = (a+b+c)
arr = [0] * (total)
comparison = 0
max_index = len()
for i in range(1,a+1):
    for j in range(1,b+1):
        for k in range(1,c+1):
            arr[i+j+k-1] +=1
            if( arr[(i+j+k-1)]>= arr[max_index]):
                if(max_index > i+j+k-1):
                    max_index = i+j+k-1

print(arr[max_index])
