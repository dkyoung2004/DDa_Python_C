a,b,c = list(map(int,input().split()))
total = (a+b+c)
arr = [0] * (total)
comparison = 0
for i in range(1,a+1):
    for j in range(1,b+1):
        for k in range(1,c+1):
            arr[i+j+k-1] +=1
    
#이런거 반환하는 함수는 대부분 제일 작은수 뽑아주니까 굳이 비교하는 
#코딩을 할 필요가 없음.
print(arr.index(max(arr))+1)
