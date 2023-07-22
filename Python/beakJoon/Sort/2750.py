N = int(input())
array = []
for i in range(0,N):
    array.append(int(input()))
for i in range(1,N):
    var = array[i]
    for j in range(1,i+1):
        edit = array[i-j]
        if(edit > var):
            array[i-j] = var
            array[i-j+1] = edit
        else:
            break
for i in range(0,N):
    print(array[i])
