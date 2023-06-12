n=1
arr = []
arr2 = []
while True:
    n = int(input())
    if(n == 0):
        break
    arr = list(map(int,str(n)))
    arr2 = arr[::-1]
    if(arr==arr2):
        print("yes")
    else:
        print("no")