arr = list(map(int,input().split()))
arr = sorted(arr)

while (arr[2]!=0):
    if (((arr[0]**2)+(arr[1]**2))==(arr[2]**2)):
        print("right")
    else:
        print("wrong")
    arr = list(map(int,input().split()))
    arr = sorted(arr)