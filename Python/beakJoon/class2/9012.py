N = int(input())

for i in range(0,N):
    Target = list(input())
    check = 0
    for j in Target:
        if j == '(':
            check += 1
        else:
            check -=1
        if (check < 0):
            print('NO')
            break
    if check > 0:
        print('NO')
    elif check == 0 :
        print("YES")