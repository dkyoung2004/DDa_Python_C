N = int(input())
arr=[]
for i in range(0,N):
    Age, name = map(str,input().split())
    Age = int(Age)
    arr.append((Age,name))
a = sorted(arr,key = lambda x:x[0])

for i in a:
    print(i[0],i[1])