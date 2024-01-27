
def kantoar(start,n):
    if n <= 0:
        return 0
    else:
        arr[start+(3**(n-1)):start+(2*(3**(n-1)))] = [' ']*3**(n-1)
        kantoar(start,n-1)
        kantoar(start+(2*(3**(n-1))),n-1)
while True:
    try:
        N = int(input())
        arr = ['-'] * (3**N)
        kantoar(0,N)
        for i in arr:
            print(i,end='')
        print()
    except:
        break

    